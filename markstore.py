from typing import BinaryIO, Any
import io

import logging

_log = logging.getLogger("markstore")


def dump(obj: Any, fp: BinaryIO) -> None:
    """
    Dump the given object to a file as a markstored string
    
    :param obj: The object to store
    :param fp: Output file pointer or path to file
    """
    d = _MarkstoreDumper(fp)
    d._dump_obj(obj)


def load(fp: BinaryIO) -> Any:
    """
    Load the given file or path into an object.
    
    :param fp: Input file pointer
    :type fp: TextIO
    :return: The deserialized object
    :rtype: dict[str, Any]
    """
    l = _MarkstoreLoader(fp)
    return l._load_obj()


def dumps(obj: Any) -> str:
    """
    Dump the object to a markdown string
    
    :param obj: The object to store
    :type obj: dict[str, Any]
    :return: The serialized markstored string
    :rtype: str
    """
    out = io.BytesIO()
    dump(obj, out)
    return out.getvalue().decode()


def loads(data: str | bytes) -> Any:
    """
    Load the given string data as a markstored object
    
    :param data: The input markstore string
    :type data: str
    :return: The deserialized object
    :rtype: dict[str, Any]
    """
    if isinstance(data, str):
        data = data.encode()
    return load(io.BytesIO(data))


class _MarkstoreDumper:

    def __init__(self, fp: BinaryIO) -> None:
        self.fp = fp
        self.indent = 0
        self.dictDepth = [1]

        self._loggedDepth = False

    def _write_indent(self):
        for _ in range(self.indent):
            self.fp.write(b" ")

    def _inc_dict(self):
        self.dictDepth[-1] += 1
        if self.dictDepth[-1] > 6 and not self._loggedDepth:
            _log.warning(
                "markstore: dictionary depth > 6, output markdown will not conform to CommonMark standard"
            )
            self._loggedDepth = True

    def _dec_dict(self):
        self.dictDepth[-1] -= 1
        if self.dictDepth[-1] < 1:
            raise RuntimeError("DEV-ERROR: _dec_dict() called too many times")

    def _write_dict_key(self, key: str):
        for _ in range(self.dictDepth[-1]):
            self.fp.write(b"#")
        self.fp.write(b" ")
        self.fp.write(key.encode())

    def _dump_obj(self, obj):
        if isinstance(obj, list):
            for idx, item in enumerate(obj):
                self.fp.write(b"- ")
                self.indent += 2
                self._dump_obj(item)
                self.indent -= 2
                if idx + 1 < len(obj):
                    self.fp.write(b"\n")
                    self._write_indent()
        elif isinstance(obj, dict):
            for idx, (key, value) in enumerate(obj.items()):
                self._write_dict_key(key)
                self.fp.write(b"\n")
                self._write_indent()
                self._inc_dict()
                self._dump_obj(value)
                self._dec_dict()

                if idx + 1 < len(obj):
                    self.fp.write(b"\n\n")
                    self._write_indent()

        elif isinstance(obj, str):
            lines = obj.splitlines(keepends=True)
            for idx, line in enumerate(lines):
                self.fp.write(line.encode())
                if idx + 1 < len(lines):
                    self._write_indent()

        elif isinstance(obj, float) or isinstance(obj, int):
            self.fp.write(str(obj).encode())
        else:
            # TODO error if unknown type?
            # Maybe just convert it to a string?
            pass


class _MarkstoreLoader:

    def __init__(self, fp: BinaryIO) -> None:
        self.fp = fp
        self.indent = 0
        self.dictDepth = 0
        self.alreadyReadDict = 0

    def _consume_indent(self, amount: int) -> int:
        out = 0
        while out < amount:
            c = self.fp.read(1)
            if len(c) == 0:
                break
            if c == b' ':
                out += 1
            else:
                self._unget()
                break
        return out

    def _unget(self):
        self.fp.seek(self.fp.tell() - 1, 0)

    def _load_obj(self) -> Any:
        obj = None

        c = self.fp.read(1)
        if len(c) == 0:
            return None
        # First char will be #, -, or else it is a string
        if c == b'#':
            obj = {}
            expectedDepth = self.dictDepth + 1
            expectedIndent = self.indent
            self.dictDepth += 1
            while c == b'#':
                dictDepth = 1
                while True:
                    c = self.fp.read(1)
                    if c != b'#':
                        break
                    dictDepth += 1

                if c != b' ':
                    self._unget()
                if dictDepth > expectedDepth:
                    raise RuntimeError("Unexpected dictionary key depth")
                elif dictDepth < expectedDepth:
                    self.alreadyReadDict = dictDepth
                    break

                key = self.fp.readline().rstrip().decode()
                newIndent = self._consume_indent(expectedIndent)
                if newIndent < expectedIndent:
                    raise RuntimeError("Unexpected unindent")

                value = self._load_obj()
                obj[key] = value
                if self.alreadyReadDict != 0:
                    if self.alreadyReadDict > expectedDepth:
                        raise RuntimeError("Unexpected dictionary key depth")
                    elif self.alreadyReadDict < expectedDepth:
                        break
                    else:
                        self.alreadyReadDict = 0
                        c = b'#'
                else:
                    c = self.fp.read(1)
                    if c == b'\n':
                        # TODO is this bad? check indent?
                        newIndent = self._consume_indent(expectedIndent)
                        if newIndent < expectedIndent:
                            self.indent = newIndent
                            break
                        c = self.fp.read(1)
                    if c != b'#':
                        self._unget()
                        break

            self.dictDepth -= 1

        elif c == b'-':
            obj = []
            while c == b'-':
                self.indent += 2
                curIndent = self.indent
                temp = self.fp.read(1)
                if temp != b' ':
                    self._unget()
                obj.append(self._load_obj())
                if self.indent != curIndent - 2:
                    break
                c = self.fp.read(1)
                if len(c) == 0:
                    break
                if c == b'\n':
                    c = self.fp.read(1)
                if c != b'-':
                    self._unget()
                    break

        else:
            # It's a string
            # Read lines until we hit an important char
            obj = c + self.fp.readline()
            while True:
                newIndent = self._consume_indent(self.indent)
                if newIndent != self.indent:
                    self.indent = newIndent
                    break
                c = self.fp.read(1)

                if c in (b'#', b'-'):
                    self._unget()
                    break
                if c != b'\n':
                    new_line = c + self.fp.readline()
                else:
                    new_line = c
                if len(new_line) == 0:
                    break
                else:
                    obj += new_line
            obj = obj.decode().rstrip()

        return obj

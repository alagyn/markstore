from typing import TextIO, Any
from io import StringIO

import logging

_log = logging.getLogger("markstore")


def dump(obj: Any, fp: TextIO) -> None:
    """
    Dump the given object to a file as a markstored string
    
    :param obj: The object to store
    :param fp: Output file pointer or path to file
    """
    d = _MarkstoreDumper(fp)
    d._dump_obj(obj)


def load(fp: TextIO) -> Any:
    """
    Load the given file or path into an object.
    
    :param fp: Input file pointer
    :type fp: TextIO
    :return: The deserialized object
    :rtype: dict[str, Any]
    """
    out: dict[str, Any] = {}

    return out


def dumps(obj: Any) -> str:
    """
    Dump the object to a markdown string
    
    :param obj: The object to store
    :type obj: dict[str, Any]
    :return: The serialized markstored string
    :rtype: str
    """
    out = StringIO()
    dump(obj, out)
    return out.getvalue()


def loads(data: str) -> Any:
    """
    Load the given string data as a markstored object
    
    :param data: The input markstore string
    :type data: str
    :return: The deserialized object
    :rtype: dict[str, Any]
    """
    return load(StringIO(data))


class _MarkstoreDumper:

    def __init__(self, fp: TextIO) -> None:
        self.indent = 0
        self.fp = fp
        self.dictDepth = [1]

        self._loggedDepth = False

    def _write_indent(self):
        for _ in range(self.indent):
            self.fp.write(" ")

    def _push_dict(self):
        self.dictDepth.append(1)

    def _pop_dict(self):
        self.dictDepth.pop()

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
            self.fp.write("#")
        self.fp.write(" ")
        self.fp.write(key)

    def _dump_obj(self, obj):
        if isinstance(obj, list):
            for idx, item in enumerate(obj):
                self.fp.write("- ")
                self.indent += 2
                self._push_dict()
                self._dump_obj(item)
                self._pop_dict()
                self.indent -= 2
                if idx + 1 < len(obj):
                    self.fp.write("\n")
                    self._write_indent()
        elif isinstance(obj, dict):
            for idx, (key, value) in enumerate(obj.items()):
                self._write_dict_key(key)
                self._inc_dict()
                self._dump_obj(value)
                self._dec_dict()

        elif isinstance(obj, str):
            self.fp.write(obj)
        else:
            pass

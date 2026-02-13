import os
import unittest

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

import markstore


def get_data(name: str) -> str:
    out = os.path.join(DATA_DIR, name)
    if not os.path.exists(out):
        raise RuntimeError(f"Cannot find test data file: {out}")
    return out


def test_serialize(file: str, expected):

    def _test(self: unittest.TestCase):
        with open(get_data(file), mode='r') as f:
            expected_file = f.read()

        out = markstore.dumps(expected)

        self.assertEqual(expected_file, out)

    return _test


def test_deserialize(file: str, expected):

    def _test(self: unittest.TestCase):
        with open(get_data(file), mode='rb') as f:
            data = markstore.load(f)

        self.assertEqual(expected, data)

    return _test

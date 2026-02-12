import unittest

import markstore

from utils import get_data

FILE_BASIC = get_data("basic.md")
EXPECTED_BASIC = {
    "My Key":
    "My Data",
    "Data": {
        "Subdata": {
            "Leaf": "This here is my data"
        }
    },
    "My List": [
        "Entry one", "Entry two", {
            "Entry 3": {
                "SubEntry": "My Data is here"
            }
        }, ["sublist", "lists in lists"]
    ]
}

FILE_TRIVIAL_LIST = get_data("trivial_list.md")
EXPECTED_TRIVIAL_LIST = ["one", "two", "three"]

FILE_COMPLEX_LIST = "complex_list.md"
EXPECTED_COMPLEX_LIST = [
    "one", ["sub1", "sub2", ["subsub1", "subsub2"]], "three"
]


class TestBasic(unittest.TestCase):

    def test_basic_deserialize(self):

        with open(FILE_BASIC, mode='r') as f:
            data = markstore.load(f)

        self.assertDictEqual(EXPECTED_BASIC, data)

    def test_basic_serialize(self):
        out = markstore.dumps(EXPECTED_BASIC)

        with open(FILE_BASIC, mode='r') as f:
            expected_file = f.read()

        self.assertEqual(expected_file, out)

    def test_trivial_list_deserialize(self):

        with open(get_data(FILE_TRIVIAL_LIST), mode='r') as f:
            data = markstore.load(f)

        self.assertListEqual(EXPECTED_TRIVIAL_LIST, data)

    def test_trivial_list_serialize(self):
        with open(get_data(FILE_TRIVIAL_LIST), mode='r') as f:
            expected_file = f.read()

        out = markstore.dumps(EXPECTED_TRIVIAL_LIST)

        self.assertEqual(expected_file, out)

    def test_complex_list_deserialize(self):

        with open(get_data(FILE_COMPLEX_LIST), mode='r') as f:
            data = markstore.load(f)

        self.assertListEqual(EXPECTED_COMPLEX_LIST, data)

    def test_complex_list_serialize(self):
        with open(get_data(FILE_COMPLEX_LIST), mode='r') as f:
            expected_file = f.read()

        out = markstore.dumps(EXPECTED_COMPLEX_LIST)

        self.assertEqual(expected_file, out)

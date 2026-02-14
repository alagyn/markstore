import unittest

import markstore

from utils import get_data, test_deserialize, test_serialize

FILE_TRIVIAL_STRING = get_data("trivial_string.md")
EXPECTED_TRIVIAL_STRING = "This is just a string"

FILE_TRIVIAL_LIST = get_data("trivial_list.md")
EXPECTED_TRIVIAL_LIST = ["one", "two", "three"]

FILE_COMPLEX_LIST = get_data("complex_list.md")
EXPECTED_COMPLEX_LIST = [
    "one", ["sub1", "sub2", ["subsub1", "subsub2"]], "three"
]

FILE_TRIVIAL_DICT = get_data("trivial_dict.md")
EXPECTED_TRIVIAL_DICT = {
    "Key1": "Entry1",
    "Key2": "Entry2",
    "Key3": "Entry3",
}

FILE_COMPLEX_DICT1 = get_data("complex_dict1.md")
EXPECTED_COMPLEX_DICT1 = {
    "Key1": "Entry1",
    "Key2": {
        "Subkey1": "SubEntry1",
        "Subkey2": "SubEntry2"
    },
    "Key3": "Entry3"
}

FILE_COMPLEX_DICT2 = get_data("complex_dict2.md")
EXPECTED_COMPLEX_DICT2 = {
    "Key1": "Entry1",
    "Key2": {
        "Subkey1": "SubEntry1",
        "Subkey2": {
            "Subkey2.1": "Leaf1",
            "Subkey2.2": "Leaf2"
        }
    },
    "Key3": "Entry3"
}

FILE_COMPLICATED = get_data("complicated.md")
EXPECTED_COMPLICATED = {
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

FILE_NEGATIVE_NUMBERS = get_data("negative_numbers.md")
EXPECTED_NEGATIVE_NUMBERS = {
    "MyData": "12",
    "MyNegative": "-21",
    "MyList": ["10", "11", "-9"]
}

FILE_STRINGS_WITH_POUND = get_data("strings_with_pound.md")
EXPECTED_STRINGS_WITH_POUND = {
    "My Key": "# My string starts with #",
    "My other key": "# My other string has\n#multiple\n# pounds"
}


class TestBasic(unittest.TestCase):

    test_trivial_str_deserialize = test_deserialize(FILE_TRIVIAL_STRING,
                                                    EXPECTED_TRIVIAL_STRING)

    test_trivial_str_serialize = test_serialize(FILE_TRIVIAL_STRING,
                                                EXPECTED_TRIVIAL_STRING)

    test_trivial_list_deserialize = test_deserialize(FILE_TRIVIAL_LIST,
                                                     EXPECTED_TRIVIAL_LIST)

    test_trivial_list_serialize = test_serialize(FILE_TRIVIAL_LIST,
                                                 EXPECTED_TRIVIAL_LIST)

    test_complex_list_deserialize = test_deserialize(FILE_COMPLEX_LIST,
                                                     EXPECTED_COMPLEX_LIST)

    test_complex_list_serialize = test_serialize(FILE_COMPLEX_LIST,
                                                 EXPECTED_COMPLEX_LIST)

    test_trivial_dict_deserialize = test_deserialize(FILE_TRIVIAL_DICT,
                                                     EXPECTED_TRIVIAL_DICT)

    test_trivial_dict_serialize = test_serialize(FILE_TRIVIAL_DICT,
                                                 EXPECTED_TRIVIAL_DICT)

    test_complex_dict1_deserialize = test_deserialize(FILE_COMPLEX_DICT1,
                                                      EXPECTED_COMPLEX_DICT1)

    test_complex_dict1_serialize = test_serialize(FILE_COMPLEX_DICT1,
                                                  EXPECTED_COMPLEX_DICT1)

    test_complex_dict2_deserialize = test_deserialize(FILE_COMPLEX_DICT2,
                                                      EXPECTED_COMPLEX_DICT2)

    test_complex_dict2_serialize = test_serialize(FILE_COMPLEX_DICT2,
                                                  EXPECTED_COMPLEX_DICT2)

    test_complicated_deserialize = test_deserialize(FILE_COMPLICATED,
                                                    EXPECTED_COMPLICATED)

    test_complicated_serialize = test_serialize(FILE_COMPLICATED,
                                                EXPECTED_COMPLICATED)

    test_negative_numbers_deserialize = test_deserialize(
        FILE_NEGATIVE_NUMBERS, EXPECTED_NEGATIVE_NUMBERS)

    test_negative_numbers_serialize = test_serialize(
        FILE_NEGATIVE_NUMBERS, EXPECTED_NEGATIVE_NUMBERS)

    test_strings_with_pound_deserialize = test_deserialize(
        FILE_STRINGS_WITH_POUND, EXPECTED_STRINGS_WITH_POUND)

    test_strings_with_pound_serialize = test_serialize(
        FILE_STRINGS_WITH_POUND, EXPECTED_STRINGS_WITH_POUND)

import unittest

import markstore
from utils import get_data, test_deserialize, test_serialize

FILE_LIST_IN_DICT = get_data("list_in_dict.md")
EXPECTED_LIST_IN_DICT = {
    "Key1": "My Data",
    "Data": ["entry1", "entry2", "entry3"],
    "Key2": "Other data"
}

FILE_DICT_IN_LIST = get_data("dict_in_list.md")
EXPECTED_DICT_IN_LIST = [
    "Entry1", {
        "Key1": "Data1",
        "Key2": "Data2"
    }, "Entry3"
]

FILE_LAYERS1 = get_data("layers1.md")
EXPECTED_LAYERS1 = {
    "Key1":
    "My Data",
    "Data": [{
        "Subkey1": "Subdata1"
    }, {
        "Subkey2": {
            "Subkey2.1": "Subdata2.1",
            "Subkey2.2": "Subdata2.2"
        }
    }],
    "Key2":
    "Other data"
}


class TestMixing(unittest.TestCase):

    test_list_in_dict_deserialize = test_deserialize(FILE_LIST_IN_DICT,
                                                     EXPECTED_LIST_IN_DICT)

    test_list_in_dict_serialize = test_serialize(FILE_LIST_IN_DICT,
                                                 EXPECTED_LIST_IN_DICT)

    test_dict_in_list_deserialize = test_deserialize(FILE_DICT_IN_LIST,
                                                     EXPECTED_DICT_IN_LIST)

    test_dict_in_list_serialize = test_serialize(FILE_DICT_IN_LIST,
                                                 EXPECTED_DICT_IN_LIST)

    test_layers1_deserialize = test_deserialize(FILE_LAYERS1, EXPECTED_LAYERS1)

    test_layers1_serialize = test_serialize(FILE_LAYERS1, EXPECTED_LAYERS1)

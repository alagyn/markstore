import unittest

import markstore
from utils import get_data, test_deserialize, test_serialize

FILE_EMPTY_VALUES = get_data("empty_values.md")
EXPECTED_EMPTY_VALUES = {
    "Key1": "Data1",
    "Key2": "",
    "Key3": {
        "Key3.1": "Data2",
        "Key3.2": ""
    }
}

FILE_EMPTY_LIST = get_data("empty_list.md")
EXPECTED_EMPTY_LIST = ["Data1", "Data2", "", "Data3", ""]

FILE_EMPTY_LAYERS = get_data("empty_layers.md")
EXPECTED_EMPTY_LAYERS = {
    "Key1":
    "Data1",
    "Key2": [{
        "ListKey": "ListData",
        "EmptyKey": "",
        "Other Empty": ""
    }, ["ListData2", "", "ListData3"]]
}

FILE_EMPTY_LAYERS2 = get_data("empty_layers2.md")
EXPECTED_EMPTY_LAYERS2 = [{
    "ListKey": "ListData",
    "EmptyKey": "",
    "Other Empty": ""
}]

FILE_STRING_NEWLINES = get_data("string_newlines.md")
EXPECTED_STRING_NEWLINES = {
    "MyData": "This is my data\n",
    "MyOtherData":
    ["Data\n\n\nStuff", "Normal data\n\n", "Eggs", "On the end\n\n"]
}

FILE_EMPTY_KEY = get_data("empty_key.md")
EXPECTED_EMPTY_KEY = {
    "Key1": "Data1",
    "": "EmptyKeyData",
    "Key3": {
        "Key3.1": "Data2",
        "Key3.2": ""
    }
}


class TestEmpty(unittest.TestCase):

    test_empty_values_deserialize = test_deserialize(FILE_EMPTY_VALUES,
                                                     EXPECTED_EMPTY_VALUES)

    test_empty_values_serialize = test_serialize(FILE_EMPTY_VALUES,
                                                 EXPECTED_EMPTY_VALUES)

    test_empty_list_deserialize = test_deserialize(FILE_EMPTY_LIST,
                                                   EXPECTED_EMPTY_LIST)

    test_empty_list_serialize = test_serialize(FILE_EMPTY_LIST,
                                               EXPECTED_EMPTY_LIST)

    test_empty_layers_deserialize = test_deserialize(FILE_EMPTY_LAYERS,
                                                     EXPECTED_EMPTY_LAYERS)

    test_empty_layers_serialize = test_serialize(FILE_EMPTY_LAYERS,
                                                 EXPECTED_EMPTY_LAYERS)

    test_empty_layers2_deserialize = test_deserialize(FILE_EMPTY_LAYERS2,
                                                      EXPECTED_EMPTY_LAYERS2)

    test_empty_layers2_serialize = test_serialize(FILE_EMPTY_LAYERS2,
                                                  EXPECTED_EMPTY_LAYERS2)

    test_string_newlines_deserialize = test_deserialize(
        FILE_STRING_NEWLINES, EXPECTED_STRING_NEWLINES)

    test_string_newlines_serialize = test_serialize(FILE_STRING_NEWLINES,
                                                    EXPECTED_STRING_NEWLINES)

    test_empty_key_deserialize = test_deserialize(FILE_EMPTY_KEY,
                                                  EXPECTED_EMPTY_KEY)

    test_empty_key_serialize = test_serialize(FILE_EMPTY_KEY,
                                              EXPECTED_EMPTY_KEY)

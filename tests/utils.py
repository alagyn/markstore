import os
import unittest

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def get_data(name: str) -> str:
    out = os.path.join(DATA_DIR, name)
    if not os.path.exists(out):
        raise RuntimeError(f"Cannot find test data file: {out}")
    return out


class SimpleMarkstoreTest(unittest.TestCase):

    def __init__(self) -> None:
        pass

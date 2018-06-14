import unittest
import argparse

from umdcli import cliparse


class TestHumanSize(unittest.TestCase):
    def test_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("size",
                            action=cliparse.HumanSize,
                            nargs='?',
                            type=str,
                            default="1")
        ops = parser.parse_args(["10"])
        self.assertEqual(ops.size,10, "Int")

        ops = parser.parse_args(['1Kb'])
        self.assertEqual(ops.size,128, "Kilobit")

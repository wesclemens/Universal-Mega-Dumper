import unittest

from umdcli import util


class TestUtil(unittest.TestCase):
    def test_human_size(self):
        bit = util.human_size("10")
        kilobit = util.human_size("2Kb")
        kilobyte = util.human_size("2KB")
        megabit = util.human_size("2Mb")
        megabyte = util.human_size("2MB")

        self.assertEqual(bit, 10, "Small Size")
        self.assertEqual(kilobit, 256, "Kilobit Size")
        self.assertEqual(kilobyte, 2048, "Kilobyte Size")
        self.assertEqual(megabit, 262144, "Megabit Size")
        self.assertEqual(megabyte, 2097152, "Megabyte Size")


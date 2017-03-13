# File: test_prefixes.py
# This module tests if module all_prefixes.py works properly

from all_prefixes import all_prefixes
import unittest


class PrefixesTestCase(unittest.TestCase):
    counter = 1

    def setUp(self):
        print("Setting uo the test {} ...".format(
            PrefixesTestCase.counter))

    def tearDown(self):
        print("Test {} is finished".format(PrefixesTestCase.counter))
        PrefixesTestCase.counter += 1

    def test_not_string(self):
        self.assertEqual(all_prefixes(234), None)

    def test_1(self):
        self.assertEqual(all_prefixes("cat"), {"c", "ca", "cat"})

    def test_2(self):
        self.assertEqual(all_prefixes("alarm"), {"a", "al", "ala", "alar",
                                                 "alarm", "ar", "arm"})

    def test_3(self):
        self.assertEqual(all_prefixes("A cat"), None)

if __name__ == '__main__':
    unittest.main()

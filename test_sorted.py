# File: test_sorted.py
# This module tests if module is_sorted.py works properly

from is_sorted import is_sorted
import unittest


class ListSortedTestCase(unittest.TestCase):
    counter = 1

    def setUp(self):
        print("Setting uo the test {} ...".format(
            ListSortedTestCase.counter))

    def tearDown(self):
        print("Test {} is finished".format(ListSortedTestCase.counter))
        ListSortedTestCase.counter += 1

    def test_not_nums(self):
        self.assertEqual(is_sorted([3, "dff", 34, 54]), None)

    def test_1(self):
        self.assertEqual(is_sorted([3, 5, 5, 54]), True)

    def test_2(self):
        self.assertEqual(is_sorted([1, 1, 1, 1]), True)

    def test_3(self):
        self.assertEqual(is_sorted([3, 5, 5, 0]), False)

    def test_4(self):
        self.assertEqual(is_sorted([3, -2,  5, 5, 54]), False)
if __name__ == '__main__':
    unittest.main()

# File: test_line_intersect.py
# This module tests if module line_intersect.py works properly

from line_intersect import Line
from line_intersect import line_intersect
import unittest


class LineIntersectTestCase(unittest.TestCase):
    counter = 1

    def setUp(self):
        print("Setting uo the test {} ...".format(
            LineIntersectTestCase.counter))

    def tearDown(self):
        print("Test {} is finished".format(LineIntersectTestCase.counter))
        LineIntersectTestCase.counter += 1

    def test_no_intersection(self):
        line_1 = Line([(0.0, 0.0), (1.0, 3.0)])
        line_2 = Line([(0.0, 1.0), (1.0, 4.0)])
        self.assertEqual(line_intersect(line_1, line_2), None)

    def test_identic_lines(self):
        line_1 = Line([(0.0, 0.0), (1.0, 3.0)])
        line_2 = Line([(0.0, 0.0), (1.0, 3.0)])
        self.assertEqual(line_intersect(line_1, line_2), line_1)

    def test_invalid_line(self):
        line_1 = Line([(0.0, 0.0), (0.0, 0.0)])
        line_2 = Line([(0.0, 1.0), (2.0, 3.0)])
        self.assertEqual(line_intersect(line_1, line_2), None)

    def test_1(self):
        line_1 = Line([(0.0, 0.0), (0.3, 0.0)])
        line_2 = Line([(0.0, 1.0), (2.0, 3.0)])
        self.assertEqual(line_intersect(line_1, line_2), (-1.0, 0.0))

    def test_2(self):
        line_1 = Line([(0.0, 0.0), (1.0, 3.0)])
        line_2 = Line([(0.0, 1.0), (2.0, 3.0)])
        self.assertEqual(line_intersect(line_1, line_2), (0.5, 1.5))

    def test_3(self):
        line_1 = Line([(0.0, 0.0), (5.0, 5.0)])
        line_2 = Line([(2.0, 1.0), (6.0, 4.0)])
        self.assertEqual(line_intersect(line_1, line_2), (-2.0, -2.0))


if __name__ == '__main__':
    unittest.main()

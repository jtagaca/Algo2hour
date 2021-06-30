# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        redShirtHeights = [19, 2, 4, 6, 2, 3, 1, 1, 4]
        blueShirtHeights =  [21, 5, 4, 4, 4, 4, 4, 4, 4]
        expected = True
        actual = program.classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

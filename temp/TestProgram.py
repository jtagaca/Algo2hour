# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [2, 1, 5, 2, 3, 3, 4]
        expected = 2
        actual = program.firstDuplicateValue(input)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

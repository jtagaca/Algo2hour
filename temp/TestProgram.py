# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!
# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stairs = 4
        maxSteps = 2
        expected = 5
        actual = program.staircaseTraversal(stairs, maxSteps)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

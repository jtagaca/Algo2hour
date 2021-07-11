# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        characters = "aheaollabbhb"
        document = "hello"
        expected = True
        actual = program.generateDocument(characters, document)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

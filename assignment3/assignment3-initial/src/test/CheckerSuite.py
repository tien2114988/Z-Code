import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_no_entry_point(self):
        input = """number a
        func b(number a)
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 400))

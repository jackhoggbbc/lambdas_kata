import unittest
from solution import solution

class TestChallenge2(unittest.TestCase):
    def test_input_15(self):
        result = solution([1,2,3,4], 15)
        self.assertEqual(result, [-1,-1])

    def test_case_2(self):
        result = solution([4,3,10,2,8], 12)
        self.assertEqual(result, [2,3])


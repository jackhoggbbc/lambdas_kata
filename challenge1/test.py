import unittest
from solution import solution

class TestChallenge1(unittest.TestCase):
    def test_input_0(self):
        result = solution(0)
        self.assertEqual(result, 23571)

    def test_input_3(self):
        result = solution(3)
        self.assertEqual(result, 71113)



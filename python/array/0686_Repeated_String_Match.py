'''
24/12/2019

686. Repeated String Match - Easy

Tag: String

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.

'''
import math

# Solution
class Solution:
    '''
    Time complexity : O(N*(N+M))
    Space complexity : O(N+M)
    '''
    def repeatedStringMatch(self, A: str, B: str) -> int:
        q = math.ceil(len(B)/len(A))
        for i in range(2):
            if B in A * (q+i):
                return q+i
        return -1

# Unit Test
import unittest
class repeatedStringMatchCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_repeatedStringMatchCase(self):
        func = Solution().repeatedStringMatch
        self.assertEqual(func("abcd", "cdabcdab"), 3)

if __name__ == '__main__':
    unittest.main()
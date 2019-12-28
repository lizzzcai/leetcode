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
    def repeatedStringMatch(self, A: str, B: str) -> int:
        
        '''
        Time: O(N*(N+M)) where M N is the length of A, B.
        # len of S at most O(M+N). When checking whether B is a substring of A,
        this check takes naively the product of their lengths.
        
        SpacdL O(M+N)
        
        Now, suppose q is the least number for which len(B) <= len(A * q). 
        We only need to check whether B is a substring of A * q or A * (q+1).
        If we try k < q, then B has larger length than A * q and therefore can't be a substring.
        When k = q+1, A * k is already big enough to try all positions for B; namely, A[i:i+len(B)] == B for i = 0, 1, ..., len(A) - 1.

        '''
        # the least number for which len(B) <= len(A * q)
        q = math.ceil(len(B)/len(A))
        # As S is the repeat of A, which has period at most len(A)
        # So q + 1 is big enough to try all positions for B.
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
        self.assertEqual(func("abce", "cdabcdab"), -1)

if __name__ == '__main__':
    unittest.main()
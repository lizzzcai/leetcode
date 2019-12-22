'''
23/12/2019

1016. Binary String With Substrings Representing 1 To N - Medium

Tag: String

Given a binary string S (a string consisting only of '0' and '1's) and a positive integer N, return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.

 

Example 1:

Input: S = "0110", N = 3
Output: true
Example 2:

Input: S = "0110", N = 4
Output: false
 

Note:

1 <= S.length <= 1000
1 <= N <= 10^9
'''

# Solution
class Solution:
    '''
    Time complexity : O(S)
    Space complexity : O(N)
    '''
    def queryString(self, S: str, N: int) -> bool:
        # when N == 1
        return all(bin(i)[2:] in S for i in range(N, max(N//2 - 1, 0), -1))


# Unit Test
import unittest
class queryStringCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_queryStringCase(self):
        func = Solution().queryString
        self.assertEqual(func("1", 1), True)
        self.assertEqual(func("0110", 3), True)
        self.assertEqual(func("0110", 4), False)
        
        
if __name__ == '__main__':
    unittest.main()
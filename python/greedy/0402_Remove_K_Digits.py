'''
13/05/2020

402. Remove K Digits - Medium

Tag: Stack, Greedy

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def removeKdigits(self, num: str, k: int) -> str:
        
        q = []
        for x in num:
            while k and q and q[-1] > x:
                q.pop()
                k -= 1
            q.append(x)
        
        # if still k>0, remove from last
        if k:
            q = q[:-k]
        # remove the leading 0
        idx = 0
        while idx < len(q) and q[idx] == '0':
            idx += 1
            
        return ''.join(q[idx:]) or '0'

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.removeKdigits
            self.assertEqual(func("1432219",3), '1219')
            self.assertEqual(func("10200",1), '200')
            self.assertEqual(func("10",2), '0')
            self.assertEqual(func("9",1), '0')
            self.assertEqual(func("112",1), '11')


if __name__ == '__main__':
    unittest.main()
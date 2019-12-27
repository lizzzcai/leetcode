'''
27/12/2019

415. Add Strings - Easy

Tag: String

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
Accepted

'''

from typing import List
# Solution
class Solution:
    '''
    Time complexity : O(max(m, n))
    Space complexity : O(max(m, n))
    '''
    def addStrings(self, num1: str, num2: str) -> str:
        '''
        
            1 2 3
          + 4 5 6
            -----
            5 7 9
        '''
        
        n, m = len(num1) - 1, len(num2) - 1
        res = []
        carry = 0
        while n >= 0 or m >= 0:
            n1 = num1[n] if n >= 0 else '0'
            n2 = num2[m] if m >= 0 else '0'
            add = (ord(n1) - ord('0')) + (ord(n2) - ord('0'))
            carry, remain = divmod(add + carry, 10)
            res.append(remain)
            
            n -= 1
            m -= 1
        # add carry if have
        if carry:
            res.append(carry)
        # reverse and join as string
        return ''.join(map(str, res[::-1]))
            
        
# Unit Test
import unittest
class addStringsCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_addStringsCase(self):
        func = Solution().addStrings
        self.assertEqual(func("0", "0"), "0")
        self.assertEqual(func("123", "0"), "123")
        self.assertEqual(func("123", "456"), "579")
        self.assertEqual(func("123", "999"), "1122")


if __name__ == '__main__':
    unittest.main()
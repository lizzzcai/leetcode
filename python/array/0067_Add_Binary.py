'''
24/12/2019

67. Add Binary - Easy

Tag: Array

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

# Solution
class Solution:
    '''
    Time complexity : O(max(m,n))
    Space complexity : O(max(m,n))
    '''
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a)-1, len(b)-1
        res = []
        carry = 0
        while m >= 0 or n >= 0:
            bin_a = int(a[m]) if m >= 0 else 0
            bin_b = int(b[n]) if n >=0 else 0
            add = bin_a + bin_b + carry
            carry, remind = divmod(add, 2)
            res.append(remind)
            m -= 1
            n -= 1
        if carry:
            res.append(carry)
        res = res[::-1]
        return "".join(map(str, res))
                
                
# Unit Test
import unittest
class addBinaryCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_addBinaryCase(self):
        func = Solution().addBinary
        self.assertEqual(func("11", "1"), "100")
        self.assertEqual(func("1010", "1011"), "10101")
        self.assertEqual(func("1111", "1111"), "11110")



if __name__ == '__main__':
    unittest.main()
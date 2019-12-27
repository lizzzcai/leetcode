'''
27/12/2019

43. Multiply Strings - Medium

Tag: String

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''

from typing import List
# Solution
class Solution:
    '''
    Time complexity : O(n+m)
    Space complexity : O(n+m)
    '''
    def multiply(self, num1: str, num2: str) -> str:
        '''
              1 2 3 index i
            x 4 5 6 index j
            ------
                1 8
              1 2
            0 6
              1 5
            1 0
          0 5
            1 2
          0 8
      + 0 4
        -------------
          5 6 0 8 8
        0 1 2 3 4 5 index
        
        '''
        
        n, m = len(num1), len(num2)
        res = [0] * (m + n)
        
        for j in range(m-1, -1, -1):
            for i in range(n-1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p_curr, p_next = i+j+1, i+j
                # add carry
                sum_val = mul + res[p_curr]
                # assign the reminder at current
                res[p_curr] = sum_val % 10
                # add on the carry to the next
                res[p_next] += sum_val // 10
        
        # remove all the leading zero
        idx = 0
        for idx, val in enumerate(res):
            if val != 0:
                break
        
        return ''.join(map(str, res[idx:]))

# Unit Test
import unittest
class multiplyCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_multiplyCase(self):
        func = Solution().multiply
        self.assertEqual(func("2", "3"), "6")
        self.assertEqual(func("123", "456"), "56088")
        self.assertEqual(func("9133", "0"), "0")
        self.assertEqual(func("0", "0"), "0")



if __name__ == '__main__':
    unittest.main()
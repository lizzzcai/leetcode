"""
24/12/2018

Tag:

7. Reverse Integer - Easy

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [-2**31, 2**31-1]
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    """
    Pop and Push Digits & Check before Overflow

    Time Complexity: O(log(x)). There are roughly log10(x) digits in x.
    Space Complexity: O(1).
    """

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x > 0 else -1
        x = x * sign # convert to positive int
        #new_result, result = 0, 0
        result, tail = 0, 0
        #tail = 0
        while x != 0:
            tail = x % 10
            #new_result = result * 10 + tail
            result = result * 10 + tail
            # check overflow
            if result > 2**31:
                return 0
            #result = new_result
            x = x // 10
        return result * sign
        
class Solution1:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x > 0 else -1
        x = sign * x
        x_str = list(str(x))
        start, end = 0, len(x_str) - 1
        while start < end:
            x_str[start], x_str[end] = x_str[end], x_str[start]
            start += 1
            end -= 1
        x = int("".join(x_str))
        if x > 2**31:
            return 0
        else:
            return x * sign   

        
# Unit Test
import unittest
class ReverseIntegerCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ReferseInteger(self):
        # SOLUTION 0
        func = Solution().reverse
        self.assertEqual(func(123), 321)
        self.assertEqual(func(-321), -123)
        self.assertEqual(func(99999999999),0)
        self.assertEqual(func(1534236469), 0)



if __name__ == '__main__':
    unittest.main()

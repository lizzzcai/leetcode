"""
15/09/2019
29. Divide Two Integers - Medium
Tag: Math

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

"""

'''
i <<= 1 python

i = i * 2^1

https://stackoverflow.com/questions/22832615/what-do-and-mean-in-python

x << y
x = x * 2^y

x >> y
x = x / 2^y

'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        negative = ((dividend < 0) != (divisor < 0))
        
        dividend = divd = abs(dividend)
        divisor = divs = abs(divisor)

        res = 0
        t = 1
        while divd >= divisor:
            # minus divs from divd, divs = t * divisor,  divd = divd - divisor*t, res += t
            divd -= divs
            # add t to res
            res += t
            # double divs and t to accelerate
            divs += divs
            t += t
            if divd < divs:
                # reset the divs
                divs = divisor
                t = 1
        
        if negative:
            return max(-res, -2147483648)
        else:
            return min(res, 2147483647)



# Unit Test
import unittest
class divideCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_divide(self):
        func = Solution().divide
        # test 1
        self.assertEqual(func(10, 3), 3)

        # test 2
        self.assertEqual(func(7, -3), -2)

        self.assertEqual(func(0, -3), 0)

        self.assertEqual(func(-2147483648, -1), 2147483647)



if __name__ == '__main__':
    unittest.main()
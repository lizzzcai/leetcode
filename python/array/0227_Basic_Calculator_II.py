"""
21/09/2019
227. Basic Calculator II - Medium
Tag: Array, stack


Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.

"""

from typing import List
class Solution:
    def calculate(self, s: str) -> int:
        
        stack, num, sign = [], 0, '+'
        
        for i in range(len(s)):
            if  s[i].isdigit():
                num = 10*num + int(s[i])
            print(f"i:{i}, s:{s[i]}, num:{num}, sign:{sign}")
            if s[i] in '+-*/' or i == len(s)-1:
                # here we use the sign before the num, get from the end of last num
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else: # '/'
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i] # next sign: the sign behind the num
            print(f"sign: {sign}, stack: {stack}")
        
        print(stack)
        return sum(stack)


# Unit Test
import unittest
class calculateCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_calculate(self):
        func = Solution().calculate
        self.assertEqual(func("3+2*2"), 7)
        self.assertEqual(func("3/2"), 1)
        self.assertEqual(func("3+5 / 2"), 5)
        self.assertEqual(func(" "), 0)
        self.assertEqual(func(" 1"), 1)











if __name__ == '__main__':
    unittest.main()



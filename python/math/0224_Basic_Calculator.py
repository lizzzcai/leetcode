'''18/03/2020

224. Basic Calculator - Hard

Tag: Math, Stack

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.

'''

from typing import List
# Solution
class Solution1:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0 # for on-going result
        operand = 0
        sign = 1 # 1 is positive, -1 is negative
        
        for ch in s:
            if ch.isdigit():
                operand = operand * 10 + int(ch)
            elif ch == "+":
                # save the result
                res += sign * operand
                # set sign to +
                sign = 1
                # reset operand
                operand = 0
            elif ch == "-":
                # save the result
                res += sign * operand
                # set sign to +
                sign = -1
                # reset operand
                operand = 0
            elif ch == "(":
                # push the res and sign into stack
                # later pop sign first then res
                stack.append(res)
                stack.append(sign)
                
                # reset the res and sign to begin the sub-expression
                sign = 1
                res = 0
            elif ch == ")":
                # res of sub-expression
                res += sign * operand
                # sign of sub-expression            
                res *= stack.pop()
                # previous res + sign * (sub res)
                res += stack.pop()
                
                # reset operand
                operand = 0
                
        
        return res + sign * operand
                

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.calculate
            self.assertEqual(func("1 + 1"), 2)
            self.assertEqual(func("2 - 1 + 2"), 3)
            self.assertEqual(func("(1+(4+5+2)-3)+(6+8)"), 23)
            self.assertEqual(func("1"), 1)
            self.assertEqual(func("6666"), 6666)




if __name__ == '__main__':
    unittest.main()
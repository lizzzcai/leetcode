"""
15/09/2019
150. Evaluate Reverse Polish Notation - Medium
Tag: Other, Stack

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

"""

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operator = ['+', '-', '*', '/']
        stack = []
        for token in tokens:
            if token in operator: # len(stack) > 1
                # stack FILO, so it is operand2 in front of operand 1
                operand1 = stack.pop()
                operand2 = stack.pop()
                if token == '+':
                    stack.append(operand2 + operand1)
                elif token == '-':
                    stack.append(operand2 - operand1)
                elif token == '*':
                    stack.append(operand2 * operand1)

                else:
                    # stack FILO, os it is operand2 / operand 1
                    # int to truncate towards zero
                    stack.append(int(operand2 / operand1))
            else:# it is a operand
                stack.append(int(token))
        
        return stack.pop()
        
        
        
        
        

# Unit Test
import unittest
class evalRPNCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_evalRPN(self):
        func = Solution().evalRPN
 
        self.assertEqual(func(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)
        self.assertEqual(func(["4","3","-"]), 1)
        self.assertEqual(func(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(func(["4", "13", "5", "/", "+"]), 6)








if __name__ == '__main__':
    unittest.main()



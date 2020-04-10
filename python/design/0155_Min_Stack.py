'''
10/04/2020

155. Min Stack - Easy

Tag: Stack, Design 

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
 

'''

from typing import List
# Solution
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] #(val, curr_min)
        

    def push(self, x: int) -> None:
        if self.stack and x > self.stack[-1][1]:
            self.stack.append((x, self.stack[-1][1]))
        else:
            self.stack.append((x, x))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        obj = MinStack()
        obj.push(-2)
        obj.push(0)
        obj.push(-3)
        self.assertEqual(obj.getMin(), -3)
        obj.pop()
        self.assertEqual(obj.top(), 0)
        self.assertEqual(obj.getMin(), -2)


if __name__ == '__main__':
    unittest.main()
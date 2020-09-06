'''
05/09/2020

232. Implement Queue using Stacks - Easy

Tag: Stack, Design

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''

from typing import List
# Solution

import collections
class MyQueue1:
    '''
    (Two Stacks, push - O(n), pop O(1) )
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.front = None
        

    def push(self, x: int) -> None:
        """
        O(n)
        Push element x to the back of queue.
        """
        if not self.stack1:
            self.front = x

        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        self.stack2.append(x)
        
        while self.stack2:
            self.stack1.append(self.stack2.pop())

        

    def pop(self) -> int:
        """
        O(1)
        Removes the element from in front of queue and returns that element.
        """
        pop = self.stack1.pop()
        if self.stack1:
            self.front = self.stack1[-1]
        return pop
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.front
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0


class MyQueue2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.front = None
        

    def push(self, x: int) -> None:
        """
        O(1)
        Push element x to the back of queue.
        """
        if not self.stack1:
            self.front = x
        self.stack1.append(x)
        

    def pop(self) -> int:
        """
        O(1)
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2:
            return self.stack2[-1]
        return self.front
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0
        


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [MyQueue1(), MyQueue2()]:
            func = Sol
            func.push(1)
            func.push(2)
            self.assertEqual(func.peek(), 1)
            self.assertEqual(func.pop(), 1)
            self.assertEqual(func.empty(), False)


if __name__ == '__main__':
    unittest.main()
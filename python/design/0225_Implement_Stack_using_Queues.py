'''
05/09/2020

225. Implement Stack using Queues - Easy

Tag: Stack, Design

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

'''

from typing import List
# Solution

import collections
class MyStack1:
    '''
    (Two Queues, push - O(n), pop O(1) )
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = collections.deque([])
        self.q2 = collections.deque([])


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        
        '''
        O(n)
        '''
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        # swap
        self.q1, self.q2 = self.q2, self.q1
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        '''
        O(1)
        '''
        return self.q1.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0
        

class MyStack2:
    '''
    (Two Queues, push - O(1), pop O(n) )
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = collections.deque([])
        self.q2 = collections.deque([])
        self._top = None
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        
        '''
        O(1)
        '''
        self.q1.append(x)
        self._top = x
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        '''
        O(n)
        '''
        
        while len(self.q1) > 1:
            self._top = self.q1.popleft()
            self.q2.append(self._top)
        
        pop = self.q1.pop()
        self.q1, self.q2 = self.q2, self.q1
        return pop
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._top
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0


class MyStack3:
    '''
    (One Queue, push - O(n), pop O(1) )
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque([])


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        
        '''
        O(n)
        '''
        self.q.append(x)
        size = len(self.q)
        while size > 1:
            self.q.append(self.q.popleft())
            size -= 1
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        '''
        O(1)
        '''
        return self.q.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [MyStack1(), MyStack2(), MyStack3()]:
            func = Sol
            func.push(1)
            func.push(2)
            self.assertEqual(func.top(), 2)
            self.assertEqual(func.pop(), 2)
            self.assertEqual(func.empty(), False)


if __name__ == '__main__':
    unittest.main()
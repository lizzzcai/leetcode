'''
17/06/2020

716. Max Stack - Easy

Tag: Stack, Design 

Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
 
'''

from typing import List
# Solution
class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.size = 0
        self.data = [] #(val, curr_max_idx)
    
    def push(self, x:int) -> None:
        if not self.data:
            self.data.append((x,self.size))
        else:
            curr_max_idx = self.data[-1][1]
            curr_max = self.data[curr_max_idx][0]
            if x >= curr_max:
                self.data.append((x, self.size))
            else:
                self.data.append((x, curr_max_idx))
        
        self.size += 1
    
    def pop(self) -> int:
        return self.data.pop()[0]
    
    def top(self) -> int:
        return self.data[-1][0]
    
    def peekMax(self) -> int:
        # self.data[-1][1]: index of the max element
        return self.data[self.data[-1][1]][0]
        
    def popMax(self) -> int:
        max_idx = self.data[-1][1]
        item_after_max = []
        step = self.size - max_idx - 1
        while step > 0:
            item_after_max.append(self.data.pop())
            step -= 1
            self.size -= 1
        # pop the top max
        top_max = self.data.pop()
        self.size -= 1
        
        # append the rest to the stack
        while item_after_max:
            self.push(item_after_max.pop()[0])
        
        return top_max[0]


class MaxStack2(list):
    def push(self, x):
        m = max(x, self[-1][1] if self else None)
        self.append((x, m))

    def pop(self):
        return list.pop(self)[0]

    def top(self):
        return self[-1][0]

    def peekMax(self):
        return self[-1][1]

    def popMax(self):
        m = self[-1][1]
        b = []
        while self[-1][0] != m:
            b.append(self.pop())

        self.pop()
        map(self.push, reversed(b))
        return m

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        stack = MaxStack()
        stack.push(5)
        stack.push(1)
        stack.push(5)
        top1 = stack.top()
        self.assertEqual(top1, 5)
        max1 = stack.popMax()
        self.assertEqual(max1, 5)
        top2 = stack.top()
        self.assertEqual(top2, 1)
        max2 = stack.peekMax()
        self.assertEqual(max2, 5)
        pop1 = stack.pop()
        self.assertEqual(pop1, 1)
        top3 = stack.top()
        self.assertEqual(top3, 5)



if __name__ == '__main__':
    unittest.main()
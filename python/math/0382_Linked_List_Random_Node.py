'''
08/02/2020

382. Linked List Random Node - Medium

Tag: Reservoir Sampling

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();


'''

from typing import List
# Solution
from random import randrange
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        '''
        Revervoir Sampling Prove:
        https://www.youtube.com/watch?v=Ybra0uGEkpM 

        https://leetcode.com/problems/linked-list-random-node/discuss/85659/Brief-explanation-for-Reservoir-Sampling
          1/i * (1 - 1/(i+1)) * (1 - 1/(i+2)) * ... * (1 - 1/n)
        = 1/i * i/(i+1) * (i+1)/(i+2) * ... * (n-1)/n
        = 1/n
        
        '''
        p = self.head
        i, res = 0, None
        while p:
            i += 1
            if randrange(1, i+1) == i:
                res = p.val
            p = p.next
        
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)

        # Your Solution object will be instantiated and called as such:
        obj = Solution(head)
        param_1 = obj.getRandom()

        self.assertIn(param_1, [0,1,2])

if __name__ == '__main__':
    unittest.main()
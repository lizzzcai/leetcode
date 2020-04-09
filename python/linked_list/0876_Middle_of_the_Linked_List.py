'''
09/04/2020

876. Middle of the Linked List - Easy

Tag: Linked List

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Note:

The number of nodes in the given list will be between 1 and 100.

'''

from typing import List
from linked_list_utils import list_to_linkedlist, linkedlist_to_list
# Solution
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def middleNode(self, head: ListNode) -> ListNode:
        '''
        Time O(N)
        Space O(1)
        '''
        fast = slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
            
        
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.middleNode
            self.assertEqual(func(list_to_linkedlist([1,2,3,4,5])).val, 3)
            self.assertEqual(func(list_to_linkedlist([1,2,3,4,5,6])).val, 4)
            self.assertEqual(func(list_to_linkedlist([1])).val, 1)

if __name__ == '__main__':
    unittest.main()
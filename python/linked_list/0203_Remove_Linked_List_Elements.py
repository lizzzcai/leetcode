'''
20/07/2020

203. Remove Linked List Elements - Easy

Tag: Linked List

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

'''

from typing import List
from linked_list_utils import list_to_linkedlist, linkedlist_to_list, ListNode
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        curr = head
        
        while curr:
            nxt = curr.next
            if curr.val == val:
                prev.next = nxt
                curr = nxt
            else:
                prev = curr
                curr = nxt
        
        return dummy.next
        
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.removeElements
            self.assertEqual(linkedlist_to_list(func(list_to_linkedlist([1,2,6,3,4,5,6]), 6)), [1,2,3,4,5])

if __name__ == '__main__':
    unittest.main()
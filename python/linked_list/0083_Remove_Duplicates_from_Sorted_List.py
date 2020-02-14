'''
14/02/2020

83. Remove Duplicates from Sorted List - Easy

Tag: Linked List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''

from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution0:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        curr, prev = head, head
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return head

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        Time: O(n)
        Space: O(1)
        '''
        p = head
        while p and p.next:
            if p.next.val == p.val:
                p.next = p.next.next
            else:
                p = p.next
        
        return head
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().deleteDuplicates
        head = ListNode(1)
        self.assertEqual(func(head), head)
        self.assertEqual(func(None), None)

        n1 = ListNode(1)
        n2 = ListNode(1)
        n3 = ListNode(2)
        n4 = ListNode(3)
        n5 = ListNode(3)
        n1.next = n2
        n2.next = n3
        n4.next = n4
        head = n1
        src = []
        while n1:
            src.append(n1.val)
            n1 = n1.next
        res = func(head)
        dst = []
        while res:
            dst.append(res.val)
            res = res.next
        
        self.assertEqual(src, dst)
        
        
        
        

if __name__ == '__main__':
    unittest.main()
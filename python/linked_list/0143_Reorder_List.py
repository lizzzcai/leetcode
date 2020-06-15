"""
14/06/2020
143. Reorder List - Medium
Tag: Linked list

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List
class Solution:
    '''
    Time:  O(n)
    Space: O(1)
    '''
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        a, b = self.split_list(head)
        
        b = self.reverse_list(b)
        
        self.merge_list(a, b)
        
    
    def split_list(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        nxt = slow.next
        slow.next = None
        return head, nxt
    
    def reverse_list(self, head):
        prev, curr, nxt = None, head, None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
    
    def merge_list(self, a, b):

        while a and b:
            a.next, a = b, a.next
            b.next, b = a, b.next


def list_to_linkedlist(val_list):
    head = node = ListNode(None)
    for val in val_list:
        node.next = ListNode(val)
        node = node.next
    return head.next

def linkedlist_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


# Unit Test
import unittest
class sortListCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sortList(self):
        func = Solution().reorderList
        l1 = list_to_linkedlist([1,2,3,4])
        func(l1)
        res = list_to_linkedlist([1,4,2,3])
        self.assertEqual(linkedlist_to_list(l1), linkedlist_to_list(res))


if __name__ == '__main__':
    unittest.main()



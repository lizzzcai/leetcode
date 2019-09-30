"""
30/09/2019
21. Merge Two Sorted Lists - Easy
Tag: Linked list

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = node = ListNode(None)
        while l1 and l2:
            if l1.val > l2.val:
                node.next = ListNode(l2.val)
                l2 = l2.next
            else:
                node.next = ListNode(l1.val)
                l1 = l1.next
            node = node.next
        
        if l1:
            node.next = l1
        if l2:
            node.next = l2
        return head.next



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
class mergeTwoListsCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mergeTwoLists(self):
        func = Solution().mergeTwoLists
        l1 = list_to_linkedlist([1,2,4])
        l2 = list_to_linkedlist([1,3, 4])
        out = func(l1, l2)
        res = list_to_linkedlist([1,1,2,3,4,4])

        self.assertEqual(linkedlist_to_list(out), linkedlist_to_list(res))




if __name__ == '__main__':
    unittest.main()



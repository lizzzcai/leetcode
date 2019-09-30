"""
30/09/2019
23. Merge k Sorted Lists - Hard
Tag: Linked list

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        
        head = node = ListNode(0)
        for n in sorted(nodes):
            node.next = ListNode(n)
            node = node.next
        
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
class mergeKListsCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mergeKLists(self):
        func = Solution().mergeKLists
        l1 = list_to_linkedlist([1,4,5])
        l2 = list_to_linkedlist([1,3,4])
        l3 = list_to_linkedlist([2,6])
        out = func([l1,l2,l3])
        res = list_to_linkedlist([1,1,2,3,4,4,5,6])

        self.assertEqual(linkedlist_to_list(out), linkedlist_to_list(res))




if __name__ == '__main__':
    unittest.main()



"""
15/06/2020
82. Remove Duplicates from Sorted List II - Medium
Tag: Linked list

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
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
    Space: O(n)
    '''
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        hm = {}
        count = {}
        while head:
            if head.val not in count:
                count[head.val] = 1
            else:
                count[head.val] += 1
            hm[head.val] = head
            head = head.next
        
        dummy = curr = ListNode(None)
        for k, v in count.items():
            if count[k] == 1:
                curr.next = hm[k]
                curr = curr.next
        
        curr.next = None
        
        return dummy.next
        
        
        


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
        func = Solution().deleteDuplicates
        l1 = list_to_linkedlist([1,2,3,3,4,4,5])
        src = func(l1)
        res = list_to_linkedlist([1,2,5])
        self.assertEqual(linkedlist_to_list(src), linkedlist_to_list(res))


if __name__ == '__main__':
    unittest.main()



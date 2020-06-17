"""
15/06/2020
61. Rotate List - Medium
Tag: Linked list

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
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
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return head
        
        # count how many items, and get the last node
        n = 0
        tmp = head
        prev = None
        while tmp:
            prev = tmp
            tmp = tmp.next
            n+=1
        
        # connect last node to head
        prev.next = head
        
        # calculate which node will be the new end node
        # k%n is the actual move
        idx = n - k % n - 1
        
        tmp = head
        while idx > 0:
            tmp = tmp.next
            idx -= 1
        
        # new head
        head = tmp.next
        # new end
        tmp.next = None
        
        return head
        
        
        


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
        func = Solution().rotateRight
        l1 = list_to_linkedlist([1,2,3,4,5])
        src = func(l1, 2)
        res = list_to_linkedlist([4,5,1,2,3])
        self.assertEqual(linkedlist_to_list(src), linkedlist_to_list(res))


if __name__ == '__main__':
    unittest.main()



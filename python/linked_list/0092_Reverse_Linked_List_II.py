"""
14/06/2020
92. Reverse Linked List II - Medium
Tag: Linked list

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        '''
        
        1->2->3->4->5->null
        1  2<-3<-4 5->null
        1->4->3->2->5->NULL
        
        
        '''
        if not head or not head.next:
            return head
        
        prev, curr = None, head
        
        while m > 1:
            prev = curr
            curr = curr.next
            m -= 1
            n -= 1
        
        dummy1 = prev
        dummy2 = curr
        
        while curr and n > 0:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            n -= 1
        
        if dummy1:
            dummy1.next = prev
        else:
            head = prev
            
        dummy2.next = curr
        
        
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
        func = Solution().reverseBetween
        l1 = list_to_linkedlist([1,2,3,4,5])
        src = func(l1, 2, 4)
        res = list_to_linkedlist([1,4,3,2,5])
        self.assertEqual(linkedlist_to_list(src), linkedlist_to_list(res))


if __name__ == '__main__':
    unittest.main()



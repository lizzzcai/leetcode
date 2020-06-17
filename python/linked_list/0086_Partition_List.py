'''
16/06/2020

86. Partition List - Medium

Tag: Linked List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''

from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        '''
        O(N)
        O(1)
        '''
        left = l_curr = ListNode(None)
        right = r_curr = ListNode(None)
        
        while head:
            if head.val < x:
                l_curr.next = head
                l_curr = l_curr.next
            else:
                r_curr.next = head
                r_curr = r_curr.next
        
            head = head.next
        
        l_curr.next = right.next
        r_curr.next = head
        
        return left.next
        
        

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
        func = Solution().partition
        l1 = list_to_linkedlist([1,4,3,2,5,2])
        src = func(l1)
        res = list_to_linkedlist([1,2,2,4,3,5])
        self.assertEqual(linkedlist_to_list(src), linkedlist_to_list(res))

        
        
        
        

if __name__ == '__main__':
    unittest.main()
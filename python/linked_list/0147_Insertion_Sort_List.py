"""
14/06/2020
147. Insertion Sort List - Medium
Tag: Linked list

Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
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

    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        curr = head
        
        while curr:
            p = dummy
            while p.next and p.next.val < curr.val:
                p = p.next
            
            # insert curr between prev and prev.next
            nxt = curr.next
            curr.next = p.next
            p.next = curr
            curr = nxt
        
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
        func = Solution().insertionSortList
        l1 = list_to_linkedlist([4,2,1,3])
        src = func(l1)
        res = list_to_linkedlist([1,2,3,4])
        self.assertEqual(linkedlist_to_list(src), linkedlist_to_list(res))


if __name__ == '__main__':
    unittest.main()



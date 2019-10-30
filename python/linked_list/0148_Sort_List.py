"""
30/10/2019
148. Sort List - Medium
Tag: Linked list, Sort

Sort a linked list in O(n log n) time using constant space complexity.

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
    Time:  O(n log n)
    Space: O(1)
    '''
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # find the mid
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        
        # break it into two lists
        prev.next = None
        
        # recursive into left and right list
        left = self.sortList(head)
        right = self.sortList(slow)
        
        return self.mergeSort(left, right)
    
    def mergeSort(self, leftList: ListNode, rightList: ListNode) -> ListNode:
        res = ListNode(None)
        curr = res
        
        while leftList or rightList:
            
            val_l = leftList.val if leftList else float('inf')
            val_r = rightList.val if rightList else float('inf')
            
            if val_l <= val_r:
                curr.next = leftList
                leftList = leftList.next
            else:
                curr.next = rightList
                rightList = rightList.next
            
            curr = curr.next
        
        return res.next
        



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
        func = Solution().sortList
        l1 = list_to_linkedlist([4,2,1,3])
        out = func(l1)
        res = list_to_linkedlist([1,2,3,4])
        self.assertEqual(linkedlist_to_list(out), linkedlist_to_list(res))

        l2 = list_to_linkedlist([-1,5,3,4,0])
        out = func(l2)
        res = list_to_linkedlist([-1,0,3,4,5])
        self.assertEqual(linkedlist_to_list(out), linkedlist_to_list(res))

        l3 = list_to_linkedlist([])
        out = func(l3)
        res = list_to_linkedlist([])
        self.assertEqual(linkedlist_to_list(out), linkedlist_to_list(res))


        l4 = list_to_linkedlist([3])
        out = func(l4)
        res = list_to_linkedlist([3])
        self.assertEqual(linkedlist_to_list(out), linkedlist_to_list(res))

if __name__ == '__main__':
    unittest.main()



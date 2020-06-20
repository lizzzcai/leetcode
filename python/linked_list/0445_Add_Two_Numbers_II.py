"""
17/06/2020

445. Add Two Numbers II - Medium

Tag: Linked list

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List
class Solution:
    '''
    Time:  O(n+m)
    Space: O(n+m)
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val1 = []
        val2 = []
        d1 = l1
        d2 = l2
        
        while d1:
            val1.append(d1.val)
            d1 = d1.next
        while d2:
            val2.append(d2.val)
            d2 = d2.next
            
        val1 = val1[::-1]
        val2 = val2[::-1]
        
        dummy = curr = ListNode(None)
        n1 = len(val1)
        n2 = len(val2)
        i, j = 0, 0
        carry = 0
        while i < n1 and j < n2:
            s = val1[i] + val2[j] + carry
            add, carry = s % 10, s // 10 
            curr.next = ListNode(add)
            curr = curr.next
            i += 1
            j += 1
        
        while i < n1:
            s = val1[i] + carry
            add, carry = s % 10, s // 10
            curr.next = ListNode(add)
            curr = curr.next
            i += 1
            
        while j < n2:
            s = val2[j] + carry
            add, carry = s % 10, s // 10
            curr.next = ListNode(add)
            curr = curr.next
            j += 1         
        
        if carry:
            curr.next = ListNode(carry)
            curr = curr.next
            
        
        # reverse output
        prev = None
        curr = dummy.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        two stack
        Time O(m+n)
        Space O(m+n)
        '''
        val1, val2 = [], []
        while l1:
            val1.append(l1.val)
            l1 = l1.next
        while l2:
            val2.append(l2.val)
            l2 = l2.next

        head = None
        carry = 0
        while val1 or val2 or carry:
            _sum = carry
            if val1:
                _sum += val1.pop()
            if val2:
                _sum += val2.pop()
            add, carry = _sum % 10, _sum // 10
            curr = ListNode(add)
            curr.next = head
            head = curr
        
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
        func = Solution().addTwoNumbers
        l1 = list_to_linkedlist([7,2,4,3])
        l2 = list_to_linkedlist([5,6,4])
        src = func(l1,l2)
        res = list_to_linkedlist([7,8,0,7])
        self.assertEqual(linkedlist_to_list(src), linkedlist_to_list(res))

        func = Solution().addTwoNumbers
        l1 = list_to_linkedlist([5])
        l2 = list_to_linkedlist([5])
        src = func(l1,l2)
        res = list_to_linkedlist([1,0])
        self.assertEqual(linkedlist_to_list(src), linkedlist_to_list(res))

if __name__ == '__main__':
    unittest.main()



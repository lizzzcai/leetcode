"""
14/06/2020
1171. Remove Zero Sum Consecutive Nodes from Linked List - Medium
Tag: Linked list

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]
 

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
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
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        '''
        https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/discuss/366319/JavaC%2B%2BPython-Greedily-Skip-with-HashMap
        
        '''
        prefix = 0
        seen = {}
        dummy = ListNode(0)
        seen[0] = dummy
        dummy.next = head
        
        while head:
            prefix += head.val
            seen[prefix] = head # latest index of prefix
            head = head.next
        
        head = dummy
        prefix = 0
        while head:
            prefix += head.val
            # skip them all
            head.next = seen[prefix].next
            head = head.next
        
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
        func = Solution().removeZeroSumSublists
        l1 = list_to_linkedlist([1,2,-3,3,1])
        src = func(l1)
        res = list_to_linkedlist([3,1])
        self.assertEqual(linkedlist_to_list(src), linkedlist_to_list(res))


if __name__ == '__main__':
    unittest.main()



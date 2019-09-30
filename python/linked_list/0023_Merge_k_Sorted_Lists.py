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


from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem_dc:
    priority: int
    item: Any=field(compare=False)

class PrioritizedItem:
    def __init__(self, priority, item):
        self.priority = priority
        self.item = item

    def __lt__(self, other):
        return self.priority <  other.priority

class Solution1:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        piorityQ
        Time: O(Nlogk)
        Space O(1)
        '''
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put(PrioritizedItem(l.val, l))
        
        head = point = ListNode(None)
        while not q.empty():
            item = q.get()
            val, node = item.priority, item.item
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put(PrioritizedItem(node.val, node))
            
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
        func = Solution1().mergeKLists
        l1 = list_to_linkedlist([1,4,5])
        l2 = list_to_linkedlist([1,3,4])
        l3 = list_to_linkedlist([2,6])
        out = func([l1,l2,l3])
        res = list_to_linkedlist([1,1,2,3,4,4,5,6])

        self.assertEqual(linkedlist_to_list(out), linkedlist_to_list(res))




if __name__ == '__main__':
    unittest.main()



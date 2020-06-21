"""
21/06/2020

725. Split Linked List in Parts - Medium

Tag: Linked list

Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
Example 2:
Input: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
Note:

The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].
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
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        tmp = root
        n = 0
        while tmp:
            tmp = tmp.next
            n += 1
        
        min_size = n // k
        num_addon = n % k
        
        res = []
        prev, curr = None, root
        
        for i in range(k):
            res.append(curr)
            count = min_size
            while count > 0 and curr:
                prev = curr
                curr = curr.next
                count -= 1
            
            # check add on
            if i < num_addon and curr:
                prev = curr
                curr = curr.next
            
            # break the connection
            if prev:
                prev.next = None
            
        
        return res
            


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
        func = Solution().splitListToParts
        l1 = list_to_linkedlist([1,2,3,4,5,6,7,8,9,10])
        src = func(l1,3)
        src = [linkedlist_to_list(x) for x in src]
        self.assertEqual(src, [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]])


if __name__ == '__main__':
    unittest.main()



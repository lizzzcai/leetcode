'''
25/09/2020

817. Linked List Components - Medium

Tag: Linked List

We are given head, the head node of a linked list containing unique integer values.

We are also given the list G, a subset of the values in the linked list.

Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

Example 1:

Input: 
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation: 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
Example 2:

Input: 
head: 0->1->2->3->4
G = [0, 3, 1, 4]
Output: 2
Explanation: 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
Note:

If N is the length of the linked list given by head, 1 <= N <= 10000.
The value of each node in the linked list will be in the range [0, N - 1].
1 <= G.length <= 10000.
G is a subset of all values in the linked list.
'''

from typing import List
from linked_list_utils import list_to_linkedlist, linkedlist_to_list
# Solution
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        GS = set(G)
        curr = head
        ans = 0
        while curr:
            if curr.val in GS and (curr.next == None or curr.next.val not in GS):
                ans += 1
            
            curr = curr.next
        
        return ans
        
            
        
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.numComponents
            self.assertEqual(func(list_to_linkedlist([0,1,2,3]), [0,1,3]), 2)


if __name__ == '__main__':
    unittest.main()
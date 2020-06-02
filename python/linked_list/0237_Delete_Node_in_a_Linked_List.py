'''
02/06/2020

237. Delete Node in a Linked List - Easy

Tag: Linked List

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:



 

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
 

Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.

'''

from typing import List
# Solution

from linked_list_utils import ListNode, list_to_linkedlist, linkedlist_to_list
class Solution1:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            nxt = node.next
            node.val = nxt.val
            node.next =nxt.next
        else:
            node = None

class Solution2:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val, node.next = node.next.val, node.next.next

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.deleteNode
            l = list_to_linkedlist([4,5,1,9])
            target = 5
            tmp = l
            while tmp.val != target:
                tmp = tmp.next
            src = tmp
            func(src)
            self.assertEqual(linkedlist_to_list(l), [4,1,9])

if __name__ == '__main__':
    unittest.main()
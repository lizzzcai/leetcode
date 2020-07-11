"""
21/06/2020

430. Flatten a Multilevel Doubly Linked List - Medium

Tag: Linked list

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:



After flattening the multilevel linked list it becomes:


Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
Example 3:

Input: head = []
Output: []
 

How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
 

Constraints:

Number of Nodes will not exceed 1000.
1 <= Node.val <= 10^5
"""

# Definition for singly-linked list.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

from typing import List
class Solution1:
    '''
    Time:  O(n)
    Space: O(1)
    '''
    def flatten(self, head: 'Node') -> 'Node':
        
        def dfs(node):
            if node:
                while node:
                    if node.child:
                        child = node.child
                        node.child = None
                        nxt = node.next
                        node.next, child.prev = child, node
                        child_end = dfs(child)
                        child_end.next = nxt
                        if nxt:
                            nxt.prev = child_end
                        node = child_end
                    
                    if node.next:
                        node = node.next
                    else:
                        break
                        
                
                return node
            
        dfs(head)
        return head


class Solution2:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        dummy = Node(None, None, None, None)
        stack = [head]
        prev = dummy
        
        while stack:
            node = stack.pop()
            node.prev, prev.next = prev, node
            prev = node
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
                node.child = None
        
        head.prev = None
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
        for Sol in [Solution1(),Solution2()]:
            func = Sol.flatten
            l1 = Node(1, None, None, None)
            l1.next =Node(2,None, None, None)
            l1.child = Node(3,None, None, None)
            src = func(l1)

            self.assertEqual(linkedlist_to_list(src), [1,3,2])


if __name__ == '__main__':
    unittest.main()



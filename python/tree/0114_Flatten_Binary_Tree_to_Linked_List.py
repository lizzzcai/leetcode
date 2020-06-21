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
from tree_utils import TreeNode, deserialize, serialize

from typing import List
class Solution1:
    '''
    Time:  O(n)
    Space: O(1)
    '''

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/36987/Straightforward-Java-Solution
        This solution is based on recursion. We simply flatten left and right subtree and paste each sublist to the right child of the root. (don't forget to set left child to null)
        '''
        def preorder(node):
            if node:
                left = node.left
                right = node.right
                
                preorder(node.left)
                preorder(node.right)
                
                node.right = left
                node.left = None
                curr = node
                while curr.right:
                    curr = curr.right
                curr.right = right
        
        preorder(root)
        return root
                
    
class Solution2:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37154/8-lines-of-python-solution-(reverse-preorder-traversal)
        '''
        prev = None
        def preorder(node):
            nonlocal prev
            if node:
                preorder(node.right)
                preorder(node.left)

                node.right = prev
                node.left = None
                prev = node

        preorder(root)
        return root

# Unit Test
import unittest
class sortListCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sortList(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.flatten
            self.assertEqual(serialize(func(deserialize('[1,2,5,3,4,null,6]'))), serialize(deserialize('[1,null,2,null,3,null,4,null,5,null,6]')))


if __name__ == '__main__':
    unittest.main()



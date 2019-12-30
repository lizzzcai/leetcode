'''
25/12/2019

1008. Construct Binary Search Tree from Preorder Traversal - Medium

Tag: Tree, Tree Traversal

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Note: 

1 <= preorder.length <= 100
The values of preorder are distinct.

'''

from typing import List
# Solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        '''
        Time: O(n)
        Space: O(n)
        The first node in the preorder traversal is the root. put it in stack
        for the next node,
        if value < curr node, curr node.left = next node, put next node in stack
        else, pop the last node from the stack until curr node val > value.
        last pop node.right = next node, and append next node to stack
        
        '''
        root = TreeNode(preorder[0])
        stack = [root]
        for node_val in preorder[1:]:
            node = TreeNode(node_val)
            # node_val can be the left node of last node in stack
            if node_val < stack[-1].val:
                stack[-1].left = node
                stack.append(node)
            else:
                # pop stack until node_val can be the right node of the last pop
                while stack and stack[-1].val < node_val:
                    last = stack.pop()
                last.right = node
                stack.append(node)
        
        return root
            


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        '''
        recursion
        '''
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        left = [val for val in preorder[1:] if val < root_val]
        # by the definition of preorder the rest will be on the right side.
        right = preorder[1+len(left):]
        
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)
        
        return root

class Solution_is_same_tree:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        '''
        Time: O(n)
        Space: O(logn) best case, O(n), worst case
        '''
        # if p and q are both None
        if not p and not q:
            return True
        
        # if one of them are None
        if not p or not q:
            return False
        
        # if value not the same
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and \
                self.isSameTree(p.right, q.right)

# Unit Test
import unittest
class bstFromPreorderCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_bstFromPreorderCase(self):
        func = Solution().bstFromPreorder
        is_same_tree = Solution_is_same_tree().isSameTree

        dst = TreeNode(8)
        dst.left = TreeNode(5)
        dst.right = TreeNode(10)
        dst.left.left = TreeNode(1)
        dst.left.right = TreeNode(7)
        dst.right.right = TreeNode(12)

        src = func([8,5,1,7,10,12])

        self.assertEqual(is_same_tree(src, dst), True)

if __name__ == '__main__':
    unittest.main()
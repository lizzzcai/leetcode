'''
12/04/2020

543. Diameter of Binary Tree - Easy

Tag: Tree, DFS

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

'''
from tree_utils import TreeNode, deserialize
from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.ans = 1
        
        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            self.ans = max(self.ans, left+right+1)
            return max(left, right) + 1

        
        helper(root)
        return self.ans - 1

class Solution2:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.ans = 1
        
        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            self.ans = max(self.ans, left+right+1)
            return max(left, right) + 1

        
        helper(root)
        return self.ans - 1
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.diameterOfBinaryTree
            self.assertEqual(func(deserialize('[null]')), 0)
            self.assertEqual(func(deserialize('[1,2,3,4,5]')), 3)
            self.assertEqual(func(deserialize('[1,1,1,2,3,4,null,null,5]')), 5)

if __name__ == '__main__':
    unittest.main()
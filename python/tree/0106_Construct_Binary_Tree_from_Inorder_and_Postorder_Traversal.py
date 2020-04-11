'''
06/04/2020

106. Construct Binary Tree from Inorder and Postorder Traversal - Medium

Tag: Array, Tree, DFS

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

'''

from typing import List
# Solution
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        hmap = {}
        # store the indx of inorder for lookup
        for i, val in enumerate(inorder):
            hmap[val] = i
        
        n = len(postorder)
        self.i = n-1
        
        def helper(l, r):
            if self.i < 0:
                return
            if l > r:
                return None
            root = TreeNode(postorder[self.i])
            mid = hmap[root.val]
            self.i -= 1
            root.right = helper(mid+1, r)
            root.left = helper(l, mid-1)
            
            return root
        
        return helper(0, n-1)

class Solution2:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        hmap = {}
        # store the indx of inorder for lookup
        for i, val in enumerate(inorder):
            hmap[val] = i
        
        def helper(l, r):
            if not postorder:
                return
            if l > r:
                return None
            root = TreeNode(postorder.pop())
            mid = hmap[root.val]
            root.right = helper(mid+1, r)
            root.left = helper(l, mid-1)
            
            return root
        
        n = len(postorder)
        return helper(0, n-1)

def inorder_traversal(node):
    res = []
    def helper(node):
        if node:
            helper(node.left)
            res.append(node.val)
            helper(node.right)
    helper(node)
    return res

def postorder_traversal(node):
    res = []
    def helper(node):
        if node:
            helper(node.left)
            helper(node.right)
            res.append(node.val)
    helper(node)
    return res      

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.buildTree
            inorder = [9,3,15,20,7]
            postorder = [9,15,7,20,3]
            self.assertEqual(inorder_traversal(func(inorder, postorder)), inorder)
            self.assertEqual(postorder_traversal(func(inorder, postorder)), postorder)

if __name__ == '__main__':
    unittest.main()
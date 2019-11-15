'''
15/11/2019

572. Subtree of Another Tree - Easy

Tag: Tree, Recursion


Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursion
class Solution:
    '''
    https://leetcode.com/problems/subtree-of-another-tree/discuss/102724/Java-Solution-tree-traversal
    Time: O(m*n)
    Space: O(n)
    '''
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        
        return self.is_same_tree(s, t) or \
                self.isSubtree(s.left, t) or \
                 self.isSubtree(s.right, t)

        
        
    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:

        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            return  self.is_same_tree(p.left, q.left) and \
                    self.is_same_tree(p.right, q.right)
        else:
            return False
            
        


# Unit Test
import unittest
class isSubtreeCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_isSubtree(self):
        func = Solution().isSubtree



        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        q.left.left = TreeNode(2)
        q.left.right = TreeNode(2)
        q.right.right = TreeNode(3)     

        p = TreeNode(2)
        p.left = TreeNode(2)
        p.right = TreeNode(2)

        self.assertEqual(func(q, p), True)

        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        q.left.left = TreeNode(2)
        q.left.right = TreeNode(2)
        q.right.right = TreeNode(3)     

        p = TreeNode(2)
        p.left = TreeNode(2)
        p.right = TreeNode(3)

        self.assertEqual(func(q, p), False)    

        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        q.left.left = TreeNode(2)
        q.left.right = TreeNode(2)
        q.right.right = TreeNode(3)     

        p = TreeNode(2)


        self.assertEqual(func(q, p), True)    


if __name__ == '__main__':
    unittest.main()
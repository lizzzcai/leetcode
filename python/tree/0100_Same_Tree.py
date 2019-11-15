'''
15/11/2019

100. Same Tree - Easy

Tag: Tree, Recursion, Iteration

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursion
class Solution:
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

# Iteration
class Solution1:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        '''
        Time: O(n)
        Space: O(logn) best case, O(n), worst case
        '''
        def check(p, q):
            # if p and q are both None
            if not p and not q:
                return True

            # if one of them are None
            if not p or not q:
                return False

            # if value not the same
            if p.val != q.val:
                return False
            
            return True
        
        
        stack = [(p, q)]
        while stack:
            p, q = stack.pop(0)
            if not check(p, q):
                return False
            
            if p:
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))
        
        return True


# Unit Test
import unittest
class isSameTreeCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_isSameTree(self):
        func = Solution().isSameTree

        self.assertEqual(func(None, None), True)

        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        q.left.left = TreeNode(2)
        q.left.right = TreeNode(2)
        q.right.right = TreeNode(3)     

        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        p.left.left = TreeNode(2)
        p.left.right = TreeNode(2)
        p.right.right = TreeNode(3)  

        self.assertEqual(func(p, q), True)

        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        q.left.left = TreeNode(2)
        q.left.right = TreeNode(2)
        q.right.right = TreeNode(4)     

        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        p.left.left = TreeNode(2)
        p.left.right = TreeNode(2)
        p.right.right = TreeNode(3)  

        self.assertEqual(func(p, q), False)    




if __name__ == '__main__':
    unittest.main()
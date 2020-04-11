'''
11/04/2020

938. Range Sum of BST - Easy

Tag: Tree, Recursion

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.

'''

from typing import List
from tree_utils import TreeNode, deserialize

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def helper(node):
            if node:
                left_sum = helper(node.left)
                right_sum = helper(node.right)
                if L<= node.val <= R:
                    return left_sum + right_sum + node.val
                else:
                    return left_sum + right_sum
            
            else:
                return 0
        
        return helper(root)
                    
class Solution2:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def helper(node):
            if node:
                if L< node.val:
                    left_sum = helper(node.left)
                else:
                    left_sum = 0

                if node.val < R:
                    right_sum = helper(node.right)
                else:
                    right_sum = 0

                if L<= node.val <= R:
                    return left_sum + right_sum + node.val
                else:
                    return left_sum + right_sum
            
            else:
                return 0
        
        return helper(root)

class Solution3:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        if not root:
            return 0
        
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        else:
            return self.rangeSumBST(root.left, L, R) + root.val + self.rangeSumBST(root.right, L, R)


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(), Solution3()]:
            func = Sol.rangeSumBST
            root = deserialize("[10,5,15,3,7,null,18]")
            self.assertEqual(func(root, 7, 15), 32)
            root = deserialize("[10,5,15,3,7,13,18,1,null,6]")
            self.assertEqual(func(root, 6, 10), 23)

if __name__ == '__main__':
    unittest.main()
'''
01/08/2020

404. Sum of Left Leaves - Easy

Tag: Tree

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

from typing import List
from tree_utils import TreeNode, deserialize
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def helper(root, is_left):
            if not root:
                return 0
            if is_left and not root.left and not root.right:
                return root.val
            
            return helper(root.left, True) + helper(root.right, False)
        
        return helper(root.left, True) + helper(root.right, False)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.sumOfLeftLeaves
            self.assertEqual(func(deserialize("[3,9,20,null,null,15,7]")), 24)

if __name__ == '__main__':
    unittest.main()
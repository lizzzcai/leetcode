'''
08/09/2020

1022. Sum of Root To Leaf Binary Numbers - Easy

Tag: Tree

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

 

Example 1:



Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
 

Note:

The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.

'''
import collections
from typing import List
from tree_utils import TreeNode, deserialize
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        def helper(node, curr):
            if not node.left and not node.right:
                return curr*2+node.val
            
            res = 0
            if node.left:
                res += helper(node.left, curr*2+node.val)
            
            if node.right:
                res += helper(node.right, curr*2+node.val)
            
            return res
        
        return helper(root, 0)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.sumRootToLeaf
            self.assertEqual(func(deserialize('[1,0,1,0,1,0,1]')), 22)


if __name__ == '__main__':
    unittest.main()
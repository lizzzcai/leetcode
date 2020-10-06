'''
03/10/2020

530. Minimum Absolute Difference in BST - Easy

Tag: Tree

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 

Note:

There are at least two nodes in this BST.
This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
'''

from typing import List
import math
from tree_utils import TreeNode, deserialize, serialize
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def getMinimumDifference(self, root: TreeNode) -> int:
        pre = None
        ans = math.inf
        def inorder(root):
            nonlocal pre, ans
            if root:
                inorder(root.left)
                if pre == None:
                    pre = root.val
                else:
                    ans = min(ans, root.val - pre)
                    pre = root.val
                inorder(root.right)
        
        inorder(root)
        return ans

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.getMinimumDifference
            self.assertEqual(func(deserialize("[1,null,3,2]")), 1)
            self.assertEqual(func(deserialize("[543,384,652,null,445,null,699]")), 47)

if __name__ == '__main__':
    unittest.main()
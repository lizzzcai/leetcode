'''
27/06/2020

129. Sum Root to Leaf Numbers - Medium

Tag: Tree, DFS

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

'''

from typing import List
from tree_utils import TreeNode, deserialize
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(node, curr):
            nonlocal res
            curr = curr*10 + node.val
            
            if not node.left and not node.right:
                res += curr
                return
            
            if node.left:
                dfs(node.left, curr)
            if node.right:
                dfs(node.right, curr)
        
        res = 0
        dfs(root, 0)
        
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
            func = Sol.sumNumbers
            self.assertEqual(func(deserialize("[1,2,3]")), 25)
            self.assertEqual(func(deserialize("[4,9,0,5,1]")), 1026)


if __name__ == '__main__':
    unittest.main()
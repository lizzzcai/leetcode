'''
06/04/2020

113. Path Sum II - Medium

Tag: 

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''
from tree_utils import TreeNode, deserialize
from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        def dfs(node, path, curr_sum):
            
            if not node:
                return
            
            if not node.left and not node.right:
                if curr_sum == node.val:
                    res.append(path + [node.val])
            
            
            if node.left:
                dfs(node.left, path+[node.val], curr_sum-node.val)
            if node.right:
                dfs(node.right, path+[node.val], curr_sum-node.val)
        
        
        res = []
        dfs(root, [], sum)
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
            func = Sol.pathSum
            self.assertEqual(func(deserialize("[5,4,8,11,null,13,4,7,2,null,null,5,1]"), 22), [[5,4,11,2],[5,8,4,5]])

if __name__ == '__main__':
    unittest.main()
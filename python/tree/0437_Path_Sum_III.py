'''
06/04/2020

437. Path Sum III - Easy

Tag: Tree

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''
from tree_utils import TreeNode, deserialize
from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
    
        def inorder(node):
            if node:
                inorder(node.left)
                dfs(node, [], sum)
                inorder(node.right)
        
        def dfs(node, path, curr_sum):
            nonlocal res
            if not node:
                return
            
            if curr_sum == node.val:
                res += 1
                
            if node.left:
                dfs(node.left, path+[node.val], curr_sum-node.val)
            if node.right:
                dfs(node.right, path+[node.val], curr_sum-node.val)
        
        res = 0
        inorder(root)
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
            self.assertEqual(func(deserialize("[10,5,-3,3,2,null,11,3,-2,null,1]"), 8), 3)
            self.assertEqual(func(deserialize("[1,null,2,null,3,null,4,null,5]"), 3), 2)

if __name__ == '__main__':
    unittest.main()
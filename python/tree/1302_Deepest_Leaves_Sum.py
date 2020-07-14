'''
13/07/2020

1302. Deepest Leaves Sum - Medium

Tag: Tree, DFS

Given a binary tree, return the sum of values of its deepest leaves.
 

Example 1:



Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.

'''

from typing import List
import collections
from tree_utils import TreeNode, deserialize
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        sums = collections.defaultdict(int)
        max_h = 0
        
        
        def dfs(node, h, sums):
            nonlocal max_h
            
            if h > max_h:
                max_h = h
            
            if not node.left and not node.right:
                sums[h] += node.val
                return
            
            if node.left:
                dfs(node.left, h+1, sums)
            
            if node.right:
                dfs(node.right, h+1, sums)
        
        
        dfs(root, 0, sums)
        return sums[max_h]
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.deepestLeavesSum
            self.assertEqual(func(deserialize("[1,2,3,4,5,null,6,7,null,null,null,null,8]")), 15)

if __name__ == '__main__':
    unittest.main()
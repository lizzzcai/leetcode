'''
23/07/2020

103. Binary Tree Zigzag Level Order Traversal - Medium

Tag: Stack, Tree, BFS

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

from typing import List
from tree_utils import TreeNode, deserialize
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(2^(H-1))
    '''
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        stack = [root]
        direction = 1
        
        while stack:
            next_layer = []
            curr_res = []
            
            for node in stack:
                curr_res.append(node.val)
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            
            stack = next_layer
            res.append(curr_res[::direction])
            direction *= -1
            
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
            func = Sol.zigzagLevelOrder
            self.assertEqual(func(deserialize("[3,9,20,null,null,15,7]")), [[3],[20,9],[15,7]])

if __name__ == '__main__':
    unittest.main()
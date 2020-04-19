'''
19/04/2020

108. Convert Sorted Array to Binary Search Tree - Easy

Tag: Tree, DFS

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5


'''
from tree_utils import TreeNode, deserialize, serialize
from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
    
        def helper(nums,left,right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            if left == right:
                return root
            
            root.left = helper(nums, left, mid-1)
            root.right = helper(nums, mid+1, right)
            
            return root
            
        left, right = 0, len(nums)-1
        return helper(nums, left, right)


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.sortedArrayToBST
            #self.assertEqual(serialize(func([-10,-3,0,5,9])), '[0,-10,5,null,-3,null,9]')


if __name__ == '__main__':
    unittest.main()
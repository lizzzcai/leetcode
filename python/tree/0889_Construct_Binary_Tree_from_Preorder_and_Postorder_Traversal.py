'''
23/08/2020

889. Construct Binary Tree from Preorder and Postorder Traversal - Medium

Tag: Tree

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
 

Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.

'''

from typing import List
from tree_utils import TreeNode, deserialize, serialize
# Solution
class Solution1:
    '''
    Time complexity : O(n^2)
    Space complexity : O(n^2)
    '''
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        '''
        [1, 2, 3, 4, 5, 6, 7]
            1
          2   3
         4 5 6 7
         
         preorder: [1] + [2,4,5] + [3,6,7]
         postorder: [4,5,2] + [6,7,3] + [1]
         
         for each brunch, root is at the first node in preorder and last node in postorder
         if we know the root value from the preorder of the left branch,
         we go to the postorder and find the index of the root of the left branch
         we can know the length L of the left brunch
         
         so the left sub tree is pre[1:L+1], post[0:L]
         right sub tree is pre[L+1:], post[L:-1]
         
         we can use recursion to build the tree
        
        '''
        
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        
        L = post.index(pre[1]) + 1 # length of left branch
        root.left = self.constructFromPrePost(pre[1:1+L], post[:L])
        root.right = self.constructFromPrePost(pre[1+L:], post[L:-1])
        return root
        
        
            
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.constructFromPrePost
            self.assertEqual(serialize(func([1,2,4,5,3,6,7], [4,5,2,6,7,3,1])), serialize(deserialize("[1,2,3,4,5,6,7]")))





if __name__ == '__main__':
    unittest.main()
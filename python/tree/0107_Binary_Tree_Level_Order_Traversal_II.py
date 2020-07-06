'''
04/07/2020

107. Binary Tree Level Order Traversal II - Easy

Tag: Tree, BFS

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

from tree_utils import TreeNode, deserialize
from typing import List
import collections
# Solution
class Solution1:
    '''
    DFS
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            val = []
            for _ in range(len(queue)):
                pop = queue.popleft()
                val.append(pop.val)
                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)

            res.append(val)
        
        return res[::-1]

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.levelOrderBottom
            self.assertEqual(func(deserialize("[null]")), [])
            self.assertEqual(func(deserialize("[3,9,20,null,null,15,7]")), [[15,7],[9,20],[3]])
            self.assertEqual(func(deserialize("[1,2,3,4,null,null,5]")), [[4,5],[2,3],[1]])

if __name__ == '__main__':
    unittest.main()
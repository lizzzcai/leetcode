'''
24/06/2020

222. Count Complete Tree Nodes - Medium

Tag: Binary Search, Tree

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

'''
from tree_utils import TreeNode, deserialize
from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


class Solution2:
    def countNodes(self, root: TreeNode) -> int:
        '''
        Since I halve the tree in every recursive step, I have O(log(n)) steps. Finding a height costs O(log(n)). So overall O(log(n)^2).
        Time O(logn ^2)
        '''
        if not root:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        
        if left == right:
            # left is full BT
            return 1 + 2**left - 1 + self.countNodes(root.right)
        else:
            # right is full BT
            return 1 + 2**right - 1 + self.countNodes(root.left)
        
    
    def getHeight(self, node):
        if not node:
            return 0
        return 1 + self.getHeight(node.left)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.countNodes
            self.assertEqual(func(deserialize("[1,2,3,4,5,6]")), 6)

if __name__ == '__main__':
    unittest.main()
'''
02/06/2020

226. Invert Binary Tree - Easy

Tag: Tree

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

'''

from typing import List
from tree_utils import TreeNode, deserialize, serialize

# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            
            return root

class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root 

import collections
class Solution3:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        '''
        queue, Iterative
        Time O(n)
        Space O(n)
        '''
        if not root:
            return root
        
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(), Solution3()]:
            func = Sol.invertTree
            self.assertEqual(serialize(func(deserialize('[4,2,7,1,3,6,9]'))), serialize(deserialize('[4,7,2,9,6,3,1]')))

if __name__ == '__main__':
    unittest.main()
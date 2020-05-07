'''
07/05/2020

993. Cousins in Binary Tree - Easy

Tag: Tree, BFS

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.

'''

from tree_utils import TreeNode, deserialize
from typing import List
# Solution
class Solution1:
    '''
    DFS
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        def helper(node, target, h):
            if not node:
                return None, -1
            if node.left and node.left.val == target:
                return node.val, h
            if node.right and node.right.val == target:
                return node.val, h
            
            val1, h1 = helper(node.left, target, h+1)
            val2, h2 = helper(node.right, target, h+1)
            if val1:
                return val1, h1
            else:
                return val2, h2
        
        # find x
        val_x, h_x = helper(root, x, 0)
        # find y
        val_y, h_y = helper(root, y, 0)
        return h_x > 0 and h_x == h_y and val_x != val_y


class Solution2:
    '''
    dfs
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        def helper(node, parent, h, target):
            if node:
                if node.val == target:
                    return parent, h
                
                return helper(node.left, node, h+1, target) or \
                    helper(node.right, node, h+1, target)

            
        val1, h1 = helper(root, None, 0, x)
        val2, h2 = helper(root, None, 0, y)

        return h1 == h2 and val1 != val2

import collections
class Solution3:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        '''
        BFS
        '''
        q = collections.deque([root])
        while q:
            n = len(q)
            find_x, find_y = False, False
            for _ in range(n):
                node = q.popleft()
                if node.val == x:
                    find_x = True
                if node.val == y:
                    find_y = True
                    
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or \
                    (node.left.val == y and node.right.val == x):
                        return False
                    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if find_x and find_y:
                return True

        #return False

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(), Solution3()]:
            func = Sol.isCousins
            self.assertEqual(func(deserialize("[1,2,3,4]"), 4, 3), False)
            self.assertEqual(func(deserialize("[1,2,3,null,4,null,5]"), 5, 4), True)
            self.assertEqual(func(deserialize("[1,2,3,null,4]"), 2, 3), False)

if __name__ == '__main__':
    unittest.main()
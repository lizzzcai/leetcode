'''
12/04/2020

257. Binary Tree Paths - Easy

Tag: Tree, DFS

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

'''
from tree_utils import TreeNode, deserialize
from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        stack = [(root, "")]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path+str(node.val))
            if node.left:
                stack.append((node.left, path+str(node.val)+'->'))
            if node.right:
                stack.append((node.right, path+str(node.val)+'->'))
        
        return res


class Solution2:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        def dfs(node, path):
            if not node.left and not node.right:
                res.append('->'.join(map(str, path + [node.val])))
                return
            
            if node.left:
                dfs(node.left, path + [node.val])
            if node.right:
                dfs(node.right, path + [node.val])
                
        res = []
        dfs(root, [])
        return res


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.binaryTreePaths
            self.assertEqual(set(func(deserialize("[1,2,3,null,5]"))), set(["1->3","1->2->5"]))

if __name__ == '__main__':
    unittest.main()
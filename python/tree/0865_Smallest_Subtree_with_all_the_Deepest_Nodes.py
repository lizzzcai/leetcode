'''
12/04/2020

865. Smallest Subtree with all the Deepest Nodes - Medium

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
from tree_utils import TreeNode, deserialize, serialize
from typing import List
# Solution
class Solution1:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        '''
        time:O(N)
        space:O(N)
        If the node in question has maximum depth, it is the answer.

        If both the left and right child of a node have a deepest descendant, then the answer is this parent node.

        Otherwise, if some child has a deepest descendant, then the answer is that child.

        Otherwise, the answer for this subtree doesn't exist.
        
        '''
        depth = {None:-1}
        def dfs(node, parent):
            if node:
                depth[node] = depth[parent]+1
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root, None)
        max_depth = max(depth.values())
        
        def answer(node):
            if not node or depth.get(node, None) == max_depth:
                return node # otherwise None
            L, R = answer(node.left), answer(node.right)
            return node if L and R else L or R
        
        return answer(root)

import collections
class Solution2:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        '''
        We can calculate these answers disjointly for dfs(node):

        To calculate the Result.node of our answer:

        If one childResult has deeper nodes, then childResult.node will be the answer.

        If they both have the same depth nodes, then node will be the answer.

        The Result.dist of our answer is always 1 more than the largest childResult.dist we have.
        
        '''
        Result = collections.namedtuple("Result", ('node', 'dist'))
        def dfs(node):
            if not node:
                return Result(None, 0)
            L, R = dfs(node.left), dfs(node.right)
            if L.dist>R.dist:
                return Result(L.node, L.dist+1)
            if L.dist<R.dist:
                return Result(R.node, R.dist+1)
            return Result(node, L.dist+1)
        
        return dfs(root).node


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.subtreeWithAllDeepest
            self.assertEqual(serialize(func(deserialize("[3,5,1,6,2,0,8,1,null,7,4]"))), serialize(deserialize('[5,6,2,1,null,7,4]')))

if __name__ == '__main__':
    unittest.main()
'''
01/08/2020

863. All Nodes Distance K in Binary Tree - Medium

Tag: Tree, DFS, BFS

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.

'''

from typing import List
from tree_utils import TreeNode, deserialize, serialize
import collections
# Solution
class Solution1:
    '''

    If we know the parent of every node x, we know all nodes that are distance 1 from x. 
    We can then perform a breadth first search from the target node to find the answer.    
    
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        parent = dict()
        def dfs(node, par):
            parent[node] = par
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
        # save the parent node in map
        dfs(root, None)
        
        queue = collections.deque([(target, 0)])
        seen = {target}
        
        while queue:
            if queue[0][1] == K:
                return [node.val for node, _ in queue]
            
            node, d = queue.popleft()
            for nei in (node.left, node.right, parent[node]):
                if nei and nei not in seen:
                    queue.append((nei, d+1))
                    seen.add(nei)
        
        return []
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.distanceK
            root = TreeNode(3)
            target = TreeNode(5)
            root.left = target
            root.right = TreeNode(1)
            root.right.left = TreeNode(0)
            root.right.right = TreeNode(8)
            target.left = TreeNode(6)
            target.right = TreeNode(2)
            target.right.left = TreeNode(7)
            target.right.right = TreeNode(4)


            self.assertEqual(func(root, target, 2), [7,4,1])

if __name__ == '__main__':
    unittest.main()
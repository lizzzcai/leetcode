'''
08/02/2020

1110. Delete Nodes And Return Forest - Medium

Tag: Tree, DFS

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

 

Example 1:



Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.

'''

from typing import List
# Solution
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        '''
        Time: O(n)
        SpaceL O(H+M), H is the height of the tree and M is the number of node in to_delete
        
        '''
        # create set to fast search
        to_delete_set = set(to_delete)
        res = []
        
        def helper(node, is_root):
            if not node:
                return None
            
            is_deleted = node.val in to_delete
            # if node is root and will not be deleted, add into result
            if is_root and not is_deleted:
                res.append(node)
            # if the node will be deleted, then its child nodes will be the root
            node.left = helper(node.left, is_deleted)
            node.right = helper(node.right, is_deleted)
            
            # if deleted, return None
            return None if is_deleted else node
        
        helper(root, True)        
        return res

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().delNodes
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        node1 = TreeNode(6)
        node2 = TreeNode(7) 
        root.right.left = node1
        root.right.right = node2     
        to_delete = [3, 5] 
        self.assertEqual(func(root, to_delete), [root, node1, node2])

if __name__ == '__main__':
    unittest.main()
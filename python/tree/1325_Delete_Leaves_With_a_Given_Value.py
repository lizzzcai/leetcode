'''
20/01/2020

1325. Delete Leaves With a Given Value - Medium

Tag: Binary Tree, Recursion, Postorder Traversals

Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you can't).

 

Example 1:



Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
Example 2:



Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]
Example 3:



Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
Example 4:

Input: root = [1,1,1], target = 1
Output: []
Example 5:

Input: root = [1,2,3], target = 1
Output: [1,2,3]
 

Constraints:

1 <= target <= 1000
Each tree has at most 3000 nodes.
Each node's value is between [1, 1000].

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    Time complexity : O(n)
    Space complexity : O(n) if consider stack
    '''
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
        
        if root.left == None and root.right == None and root.val == target:
            return None
        else:
            return root


class Solution_sametree:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        '''
        Time: O(n)
        Space: O(logn) best case, O(n), worst case
        '''
        # if p and q are both None
        if not p and not q:
            return True
        
        # if one of them are None
        if not p or not q:
            return False
        
        # if value not the same
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and \
                self.isSameTree(p.right, q.right)


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):

        func = Solution().removeLeafNodes
        same_tree = Solution_sametree().isSameTree


        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(2)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(4)

        res = TreeNode(1)
        res.right = TreeNode(3)
        res.right.right = TreeNode(4)

        self.assertEqual(same_tree(func(root, 2), res), True)


        root = TreeNode(1)
        root.left = TreeNode(3)
        root.right = TreeNode(3)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(2)


        res = TreeNode(1)
        res.left = TreeNode(3)
        res.left.right = TreeNode(2)

        self.assertEqual(same_tree(func(root, 3), res), True)


        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)


        res = None

        self.assertEqual(same_tree(func(root, 1), res), True)

if __name__ == '__main__':
    unittest.main()
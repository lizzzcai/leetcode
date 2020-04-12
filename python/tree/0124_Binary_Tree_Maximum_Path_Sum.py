'''
15/01/2020

124. Binary Tree Maximum Path Sum -  Hard

Tag: Binary Tree, DFS, Postorder Traversals

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = root.val
        self.helper(root)
        return self.max
    
    def helper(self, node):
        if not node:
            return 0
        
        # find the max sum to left and right subtree. left and right nodes as root.
        # if the sum is negative, make it as zero. for case like [1, -2, 3]
        left = max(self.helper(node.left), 0)
        right = max(self.helper(node.right), 0)
        
        # update the max sum value by node.val + left + right, which a path between two leaves
        self.max = max(self.max, node.val + left + right)
        
        # if not subnode, return itself
        if not node.left and not node.right:
            return node.val
        
        # if has left and right, find the max sum between left and right and add the current node as the path.
        if node.left and node.right:
            return node.val + max(left, right)
        
        # if left or not is not avaiable, return root + left/right
        if node.left:
            return node.val + left
        else: # node.right
            return node.val + right
        

class Solution2:
    '''
    Time complexity : O(n)
    Space complexity : O(1)

    Postorder traversal
    '''
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = root.val
        self.helper(root)
        return self.max
    
    def helper(self, node):
        if not node:
            return 0
        
        # find the max sum to left and right subtree. left and right nodes as root.
        # if the sum is negative, make it as zero. for case like [1, -2, 3]
        left = max(self.helper(node.left), 0)
        right = max(self.helper(node.right), 0)
        
        # update the max sum value by node.val + left + right, which a path between two leaves
        self.max = max(self.max, node.val + left + right)
        
        # find the max sum between left and right and add the current node as the path.
        return node.val + max(left, right)



class Solution3:
    '''
    Time complexity : O(n)
    Space complexity : O(1)

    Postorder traversal
    '''
    def maxPathSum(self, root: TreeNode) -> int:

        def maxPath(node):
            nonlocal maxSum
            if not node:
                return 0
            
            # find the max sum to left and right subtree. left and right nodes as root.
            # if the sum is negative, make it as zero. for case like [1, -2, 3]
            left = max(self.helper(node.left), 0)
            right = max(self.helper(node.right), 0)
            
            # update the max sum value by node.val + left + right, which a path between two leaves
            self.max = max(self.max, node.val + left + right)
            
            # find the max sum between left and right and add the current node as the path.
            return node.val + max(left, right)
        
        maxSum = -math.inf
        maxPath(root)
        return maxSum

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.maxPathSum
 

            root = TreeNode(1)
            root.left = TreeNode(3)
            root.right = TreeNode(2)
            self.assertEqual(func(root), 6)

            root = TreeNode(-10)
            root.left = TreeNode(9)
            root.right = TreeNode(20)
            root.right.left = TreeNode(15)
            root.right.right = TreeNode(7)
            self.assertEqual(func(root), 42)

            root = TreeNode(0)
            self.assertEqual(func(root), 0)

            root = TreeNode(0)
            root.left = TreeNode(-1)
            root.right = TreeNode(-2)
            self.assertEqual(func(root), 0)

            root = TreeNode(1)
            root.left = TreeNode(3)
            root.right = TreeNode(-2)
            self.assertEqual(func(root), 4)

if __name__ == '__main__':
    unittest.main()
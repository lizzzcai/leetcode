'''
06/01/2020

110. Balanced Binary Tree - Easy

Tag: Tree, DFS

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        bottom up method
        Time: O(n)
        '''
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            if left == -1:
                return -1
            right = dfs(node.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1

        
        return dfs(root) != -1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        top down method
        Time: O(nlogn)
        
        I think it is NlgN for the first method. Suppose the time for isBalance is T(n), and the time for the depth function is S(n). Then we have T(n) = 2T(n/2) + 2S(n/2). We know S(n) is O(n), therefore, T(n) = 2*T(n/2) + O(n), which gives T(n) = O(n lg n) with master's theorem.
        
        I think time complexity is O(NlgN). If it is a balanced tree, there will lgN levels, every level will take O(N) to find the all the depths of each nodes, so time complexity would be O(NlgN). But if it is not a balanced tree, the recursion will stop once it finds it is not balanced, so the the complexity would be less than O(NlgN). so the time complexity is O(NlgN);
        '''
        def depth(node):
            if not node:
                return 0            
            return max(depth(node.left), depth(node.right)) + 1
        
        if not root:
            return True
        
        left = depth(root.left)
        right = depth(root.right)
        
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().isBalanced
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertEqual(func(root), True)

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)
        self.assertEqual(func(root), False)

        self.assertEqual(func(None), True)
        self.assertEqual(func(TreeNode(1)), True)


if __name__ == '__main__':
    unittest.main()
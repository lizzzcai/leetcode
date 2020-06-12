'''
12/06/2020

951. Flip Equivalent Binary Trees - Medium

Tag: Tree

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.

 

Example 1:

Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Flipped Trees Diagram
 

Note:

Each tree will have at most 100 nodes.
Each value in each tree will be a unique integer in the range [0, 99].
 
'''
from tree_utils import TreeNode, deserialize
from typing import List
# Solution
class Solution1:
    '''
    Time O(min(N1, N2))
    Space O(min(H1, H2))
    '''
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False
        
        if root1.val != root2.val:
            return False

        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) or \
                    self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
    
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.flipEquiv
            root1 = deserialize("[1,2,3,4,5,6,null,null,null,7,8]")
            root2 = deserialize("[1,3,2,null,6,4,5,null,null,null,null,8,7]")
            self.assertEqual(func(root1, root2), True)

if __name__ == '__main__':
    unittest.main()
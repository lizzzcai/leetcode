'''
09/01/2020

235. Lowest Common Ancestor of a Binary Search Tree - Easy

Tag: BST, DFS, BFS

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution0:
    '''
    Time complexity : O(n)
    Space complexity : O(n)

    Lets review properties of a BST:

    1. Left subtree of a node N contains nodes whose values are lesser than or equal to node N's value.
    2. Right subtree of a node N contains nodes whose values are greater than node N's value.
    3. Both left and right subtrees are also BSTs.

    Algorithm

    1. Start traversing the tree from the root node.
    2. If both the nodes p and q are in the right subtree, then continue the search with right subtree starting step 1.
    3. If both the nodes p and q are in the left subtree, then continue the search with left subtree starting step 1.
    4. If both step 2 and step 3 are not true, this means we have found the node which is common to node p's and q's subtrees. and hence we return this common node as the LCA.
    
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # value of current node or parent node
        parent_val = root.val
        
        # value of p
        p_val = p.val
        
        # value of q
        q_val = q.val
        
        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # we have found the split point i.e. the LCA node
        else:
            return root

class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # value of p
        p_val = p.val
        
        # value of q
        q_val = q.val
        
        # start node
        node = root
        
        while node:
            # value of current node or parent node
            parent_val = node.val
            
            # If both p and q are greater than parent
            if p_val > parent_val and q_val > parent_val:
                node = node.right
            # If both p and q are lesser than parent
            elif p_val < parent_val and q_val < parent_val:
                node = node.left

            # we have found the split point i.e. the LCA node
            else:
                return node

# Unit Test
import unittest
class lowestCommonAncestorCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_lowestCommonAncestorCase(self):
        root = TreeNode(3) # LCA
        p = TreeNode(5)
        q = TreeNode(1)
        root.left = p
        root.right = q
        p.left = TreeNode(6)
        p.right = TreeNode(2)
        p.right.left = TreeNode(7)
        p.right.right = TreeNode(4)

        q.left = TreeNode(0)
        q.right = TreeNode(8)
        func = Solution0().lowestCommonAncestor
        self.assertEqual(func(root, p ,q), root)

        func = Solution1().lowestCommonAncestor
        self.assertEqual(func(root, p ,q), root)

if __name__ == '__main__':
    unittest.main()
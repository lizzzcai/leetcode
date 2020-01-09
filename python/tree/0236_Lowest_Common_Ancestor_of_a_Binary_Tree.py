'''
09/01/2020

236. Lowest Common Ancestor of a Binary Tree - Medium

Tag: Tree, DFS, BFS

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

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

    1. Start traversing the tree from the root node.
    2. If the current node itself is one of p or q, we would mark a variable mid as True and continue the search for the other node in the left and right branches.
    3. If either of the left or the right branch returns True, this means one of the two nodes was found below.
    4. If at any point in the traversal, any two of the three flags left, right or mid become True, this means we have found the lowest common ancestor for the nodes p and q.

    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        
        def helper(current_node):
            if not current_node:
                return False
            
            left = helper(current_node.left)
            right = helper(current_node.right)
            
            mid = current_node == p or current_node == q
            
            # if any two of left, right, mid is true
            if mid + left + right >= 2:
                self.ans = current_node
                
            return mid or left or right
        
        helper(root)
        return self.ans


class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # stack for traversal
        stack =[root]
        
        # dict for parent node
        parent = {root:None}
        
        while p not in parent or q not in parent:
            node = stack.pop()
            
            # save the parent node into dict
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
                
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        # Ancestors set() for node p.
        ancestors = set()
        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]
        
        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor
        while q not in ancestors:
            q = parent[q]
        
        return q

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
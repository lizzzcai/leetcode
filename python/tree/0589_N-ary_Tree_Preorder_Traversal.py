'''
06/02/2020

589. N-ary Tree Preorder Traversal - Easy

Tag: Tree, Iterative, Recursive

Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Follow up:

Recursive solution is trivial, could you do it iteratively?

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
 

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]


'''

from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution1:
    def preorder(self, root: 'Node') -> List[int]:
        '''
        recursive
        '''
        def helper(node):
            if node:
                res.append(node.val)
                for child in node.children:
                    helper(child)
        
        res = []
        helper(root)
        return res

class Solution2:
    def preorder(self, root: 'Node') -> List[int]:
        '''
        iterative
        '''
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack += [child for child in reversed(node.children) if child]
        
        return res        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution1().preorder
        root = Node(1)
        c1 = Node(3, [Node(5, []), Node(6, [])])
        root.children = [c1, Node(2, []), Node(4, [])]
        self.assertEqual(func(root), [1,3,5,6,2,4])

        func = Solution2().preorder
        root = Node(1)
        c1 = Node(3, [Node(5, []), Node(6, [])])
        root.children = [c1, Node(2, []), Node(4, [])]
        self.assertEqual(func(root), [1,3,5,6,2,4])

if __name__ == '__main__':
    unittest.main()
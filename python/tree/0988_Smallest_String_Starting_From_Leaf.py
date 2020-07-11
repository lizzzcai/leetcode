'''
11/07/2020

988. Smallest String Starting From Leaf - Medium

Tag: Tree, DFS

Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)

 

Example 1:



Input: [0,1,2,3,4,3,4]
Output: "dba"
Example 2:



Input: [25,1,3,1,3,0,2]
Output: "adz"
Example 3:



Input: [2,2,1,null,1,0,null,0]
Output: "abc"
 

Note:

The number of nodes in the given tree will be between 1 and 8500.
Each node in the tree will have a value between 0 and 25.
'''

from typing import List
from tree_utils import TreeNode, deserialize
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ''
        
        res = None
        
        def dfs(node, path):
            nonlocal res

            if not node.left and not node.right:
                tmp = ''.join(path[::-1])
                if not res:
                    res = tmp
                else:
                    res = min(res, tmp)

                return
            
            if node.left:
                dfs(node.left, path+[chr(node.left.val + ord('a'))])
            if node.right:
                dfs(node.right, path+[chr(node.right.val + ord('a'))])          
                
        dfs(root, [chr(root.val + ord('a'))])
        return res

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.smallestFromLeaf
            self.assertEqual(func(deserialize("[3,9,20,null,null,15,7]")), 'hud')
            self.assertEqual(func(deserialize("[2,2,1,null,1,0,null,0]")), 'abc')
            self.assertEqual(func(deserialize("[25,1,3,1,3,0,2]")), 'adz')
            self.assertEqual(func(deserialize("[0,1,2,3,4,3,4]")), 'dba')




if __name__ == '__main__':
    unittest.main()
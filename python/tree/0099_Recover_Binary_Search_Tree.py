'''
23/08/2020

99. Recover Binary Search Tree - Hard

Tag: String

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
 

'''

from typing import List
from tree_utils import TreeNode, deserialize, serialize
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def recoverTree(self, root: TreeNode) -> TreeNode:
        """
        Do not return anything, modify root in-place instead.
        """
        inorders =[]
        def inorder(node):
            if node:
                inorder(node.left)
                inorders.append(node)
                inorder(node.right)
        
        inorder(root)
        x, y = None, None
        for i in range(len(inorders)-1):
            if inorders[i].val > inorders[i+1].val:
                if x == None:
                    x, y = inorders[i], inorders[i+1]
                else:
                    y = inorders[i+1]
                    break
        
        x.val, y.val = y.val, x.val
    
        return root
        
        
            
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.recoverTree
            self.assertEqual(serialize(func(deserialize("[1,3,null,null,2]"))), serialize(deserialize("[3,1,null,null,2]")))
            self.assertEqual(serialize(func(deserialize("[3,1,4,null,null,2]"))), serialize(deserialize("[2,1,4,null,null,3]")))




if __name__ == '__main__':
    unittest.main()
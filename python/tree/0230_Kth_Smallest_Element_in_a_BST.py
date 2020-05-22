'''
21/05/2020

230. Kth Smallest Element in a BST - Medium

Tag: Binary Search, Tree

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

'''

from typing import List
import math

from tree_utils import TreeNode, deserialize

class Solution1:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        
        return inorder(root)[k-1]

# Solution
class Solution2:
    '''
    Time complexity : O(logN+K)
    Space complexity : O(1)
    '''

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.left = k
        self.res = root.val
        def inorder(node):
            if node and self.left > 0:
                inorder(node.left)
                self.left -= 1
                if self.left == 0:
                    self.res = node.val
                inorder(node.right)
        
        inorder(root)
        return self.res


class Solution3:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        stack = []
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
        

class Followup:
    '''
    use doubly linked list
    '''
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        stack = []
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2(),Solution3()]:
            func = Sol.kthSmallest

            self.assertEqual(func(deserialize("[3,1,4,null,2]"),1), 1)
            self.assertEqual(func(deserialize("[5,3,6,2,4,null,null,1]"),3), 3)






if __name__ == '__main__':
    unittest.main()
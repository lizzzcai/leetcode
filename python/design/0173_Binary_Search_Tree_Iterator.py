'''
01/05/2020

173. Binary Search Tree Iterator - Medium

Tag: Tree, Stack, Design


Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize(string):
    if string == '[]':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

from typing import List
# Solution
class BSTIterator1:

    def __init__(self, root: TreeNode):
        self.root = root
        self.inorder = iter(self.__inorder(self.root))
        self.val = None
        try:
            self.val = next(self.inorder)
        except:
            self.val = None
        
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        res = self.val
        try:
            self.val = next(self.inorder)
        except:
            self.val = None
            
        return res

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.val != None
        
    def __inorder(self, node):
        if node:
            yield from self.__inorder(node.left)
            yield node.val
            yield from self.__inorder(node.right)


class BSTIterator2:

    def __init__(self, root: TreeNode):
        self.stack=[]
        self._leftmost_inorder(root)
        
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        if node.right:
            self._leftmost_inorder(node.right)
        return node.val
    
        
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [BSTIterator1,BSTIterator2]:
            func = Sol(deserialize('[7,3,15,null,null,9,20]'))
            self.assertEqual(func.next(), 3)
            self.assertEqual(func.next(), 7)
            self.assertEqual(func.hasNext(), True)
            self.assertEqual(func.next(), 9)
            self.assertEqual(func.hasNext(), True)
            self.assertEqual(func.next(), 15)
            self.assertEqual(func.hasNext(), True)
            self.assertEqual(func.next(), 20)
            self.assertEqual(func.hasNext(), False)

            func = Sol(deserialize('[]'))

            self.assertEqual(func.hasNext(), False)

if __name__ == '__main__':
    unittest.main()
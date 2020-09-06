'''
01/09/2020

1305. All Elements in Two Binary Search Trees - Medium

Tag: Tree, Sort

Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
Example 5:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

Constraints:

Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].

'''

from tree_utils import TreeNode, deserialize
from typing import List
# Solution
class Solution1:
    '''
    DFS
    Time complexity : O(n1+n2)
    Space complexity : O(n1+n2)
    '''
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root, res):
            if root:
                inorder(root.left,res)
                res.append(root.val)
                inorder(root.right, res)
                
        
        l1 = []
        inorder(root1, l1)
        
        l2 = []
        inorder(root2, l2)
        
        ans = []
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                ans.append(l1[i])
                i += 1
            else:
                ans.append(l2[j])
                j += 1
            
        while i < len(l1):
            ans.append(l1[i])
            i += 1
            
        while j < len(l2):
            ans.append(l2[j])
            j += 1
        
        return ans


class Solution2:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def gen(root):
            if root:
                yield from gen(root.left)
                yield root.val
                yield from gen(root.right)
            return
                
        gen1, gen2 = gen(root1), gen(root2)
        val1, val2 = next(gen1, None), next(gen2, None)
        ans = []
        
        while val1 != None and val2 != None:
            if val1 < val2:
                ans.append(val1)
                val1 = next(gen1, None)
            else:
                ans.append(val2)
                val2 = next(gen2, None)
        
        while val1 != None:
            ans.append(val1)
            val1 = next(gen1, None)

        while val2 != None:
            ans.append(val2)
            val2 = next(gen2, None)
        
        return ans

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.getAllElements
            self.assertEqual(func(deserialize("[2,1,4]"), deserialize("[1,0,3]")), [0,1,1,2,3,4])
            self.assertEqual(func(deserialize("[0,-10,10]"), deserialize("[5,1,7,0,2]")), [-10,0,0,1,2,5,7,10])
            self.assertEqual(func(deserialize("[null]"), deserialize("[5,1,7,0,2]")), [0,1,2,5,7])
            self.assertEqual(func(deserialize("[0,-10,10]"), deserialize("[null]")), [-10,0,10])
            self.assertEqual(func(deserialize("[1,null,8]"), deserialize("[8,1]")), [1,1,8,8])





if __name__ == '__main__':
    unittest.main()
'''
08/09/2020

652. Find Duplicate Subtrees - Easy

Tag: Tree

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

 

Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:


Input: root = [2,1,1]
Output: [[1]]
Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
 

Constraints:

The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200

'''
import collections
from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        hmap = collections.defaultdict(list)
        
        def helper(node):
            if node:
                s = f"{node.val}#{helper(node.left)}#{helper(node.right)}"
                hmap[s].append(node)
                return s
            else:
                return "$"
        
        helper(root)
        return [ hmap[node][0] for node in hmap if len(hmap[node])>1]

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.findDuplicateSubtrees


if __name__ == '__main__':
    unittest.main()
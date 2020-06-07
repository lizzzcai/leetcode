'''
07/06/2020

406. Queue Reconstruction by Height - Medium

Tag: Greedy

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

'''

from typing import List
# Solution
class Solution1:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        '''
        https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89359/Explanation-of-the-neat-Sort%2BInsert-solution
        Time: O(n^2)
        space: O(n)
        '''
        people.sort(key=lambda x : (-x[0], x[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
            
        return queue
        
class TreeNode:
    def __init__(self, lo, hi):
        self.val = 1
        self.left = None
        self.right = None
        self.lo = lo
        self.hi = hi
        
class SegmentTree:
    def __init__(self, N):
        self.root = self.build(0, N-1)
        
    def build(self, lo, hi):
        if lo == hi:
            return TreeNode(lo, hi)
        
        mid = (lo + hi) // 2
        
        node = TreeNode(lo, hi)
        
        node.left = self.build(lo, mid)
        node.right = self.build(mid+1, hi)
        
        node.val = node.left.val + node.right.val
        
        return node
    
    def query(self, node, slot):
        if node.lo == node.hi:
            node.val = 0
            return node.lo
        
        if node.left.val >= slot:
            ret = self.query(node.left, slot)
        else:
            ret = self.query(node.right, slot - node.left.val)
            
        node.val = node.left.val + node.right.val
            
        return ret

class Solution2:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        '''
        https://leetcode.com/problems/queue-reconstruction-by-height/discuss/302592/Python-From-O(N2)-Search-available-slot-to-O(NlogN)-Segment-Tree-Optimization
        '''
        if not people:
            return []
        people.sort(key = lambda x: [x[0], -x[1]])
        N = len(people)
        tree = SegmentTree(N)
        root = tree.root

        ans = [None] * N
        
        for h, k in people:
            idx = tree.query(root, k+1)
            ans[idx] = [h, k]
            
        return ans     

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.reconstructQueue
            self.assertEqual(func([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]), [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]])

if __name__ == '__main__':
    unittest.main()
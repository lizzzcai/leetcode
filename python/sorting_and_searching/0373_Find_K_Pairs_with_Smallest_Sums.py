'''
01/06/2020

373. Find K Pairs with Smallest Sums - Medium

Tag: Heap

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

'''
import heapq
from typing import List


# Solution
class Solution1:
    '''
    Time complexity : O(nlogn)
    Space complexity : O(1)
    '''
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(heap, (nums1[i]+nums2[j], i, j))
        
        push(0, 0)
        res = []
        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i] ,nums2[j]])
            push(i, j+1)
            if j == 0:
                push(i+1, 0)
        
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
            func = Sol.kSmallestPairs
            self.assertEqual(func([1,7,11], [2,4,6], 3), [[1,2],[1,4],[1,6]])
            self.assertEqual(func([1,1,2], [1,2,3], 2), [[1,1],[1,1]])


if __name__ == '__main__':
    unittest.main()
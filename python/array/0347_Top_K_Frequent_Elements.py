'''
15/04/2020

347. Top K Frequent Elements - Medium

Tag: Hash Table, Heap

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

'''
from heapq import heappop, heappush
import collections
from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        count = [(k, v) for k, v in count.items()]
        count = sorted(count, key=lambda x:x[1], reverse=True)
        
        return [count[i][0] for i in range(k)]
        

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        pq = []
        for num, freq in hmap.items():
            if len(pq) < k:
                heappush(pq, (freq, num))
            else:
                if freq > pq[0][0]:
                    heappop(pq)
                    heappush(pq, (freq, num))
        
        res = []
        while pq:
            res.append(heappop(pq)[1])
        return res[::-1]

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.topKFrequent
            self.assertEqual(func([1,1,1,2,2,3], 2), [1,2])
            self.assertEqual(func([1], 1), [1])

if __name__ == '__main__':
    unittest.main()
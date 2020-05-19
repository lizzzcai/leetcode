'''
14/05/2020

1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit - Medium

Tag: Array, Sliding Window

Given an array of integers nums and an integer limit, return the size of the longest continuous subarray such that the absolute difference between any two elements is less than or equal to limit.

In case there is no subarray satisfying the given condition return 0.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
'''

from typing import List
import heapq
# Solution
class Solution1:
    '''
    Time complexity : O(nlogn)
    Space complexity : O(n)
    '''
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minh, maxh = [], []
        res = i = 0
        
        for j, x in enumerate(nums):
            heapq.heappush(minh, (x, j))
            heapq.heappush(maxh, (-x, j))
            
            while -maxh[0][0] - minh[0][0] >limit:
                i = min(maxh[0][1], minh[0][1]) + 1
                while maxh[0][1] < i:
                    heapq.heappop(maxh)
                while minh[0][1] < i:
                    heapq.heappop(minh)
                
            res = max(res, j-i+1)
        
        return res

import collections
class Solution2:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq, maxq = collections.deque(), collections.deque()
        res = i = 0
        
        for j, x in enumerate(nums):
            
            while minq and minq[-1] > x: # ascend
                minq.pop()
            while maxq and maxq[-1] < x: # desend
                maxq.pop()          
            
            minq.append(x)
            maxq.append(x)
            
            while maxq[0] - minq[0] > limit:
                if maxq[0] == nums[i]:
                    maxq.popleft()
                if minq[0] == nums[i]:
                    minq.popleft()    
                i+=1
            res = max(res, j-i+1)
        
        return res

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.longestSubarray
            self.assertEqual(func([8,2,4,7], 4), 2)
            self.assertEqual(func([10,1,2,4,7,2], 5), 4)
            self.assertEqual(func([4,2,2,2,4,4,2,2], 0), 3)


if __name__ == '__main__':
    unittest.main()
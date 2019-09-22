"""
22/09/2019
239. Sliding Window Maximum - Hard
Tag: Array

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""

from typing import List
class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k < 1 or k > len(nums):
            raise ValueError("invalid k value, %s", k)

        # the window move len(nums) - k step, but the inital state also be considered.
        step = len(nums) - k + 1
        res = []
        for i in range(step):
            res.append(max(nums[i:i+k]))
        return res

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Monotonic Queue
        https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/204290/Monotonic-Queue-Summary

        Time: O(n)
        Space O(n)
        """
        monoQ = deque()
        res = []
        for i in range(len(nums)):
            print(f"idx:{i}, num:{nums[i]}")
            print(f"monoQ:{monoQ}")
            # if the first element of the Q is out of range, remove it
            if monoQ and monoQ[0] == i - k:
                monoQ.popleft()
            print(f"monoQ1:{monoQ}")
            # pop out element that is smaller than nums[i]
            while monoQ and nums[monoQ[-1]] < nums[i]:
                monoQ.pop()
            print(f"monoQ2:{monoQ}")
            
            #append the idx, which is the largeest
            monoQ.append(i)
            print(f"monoQ3:{monoQ}")
            if i >= k - 1:
                res.append(nums[monoQ[0]])
            print(f"res:{res}")
            
        return res

# Unit Test
import unittest
class maxSlidingWindowCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_maxSlidingWindow(self):
        func = Solution().maxSlidingWindow
        self.assertEqual(func([], 3), [])
        self.assertEqual(func([1,3,-1,-3,5,3,6,7], 3), [3,3,5,5,6,7])




if __name__ == '__main__':
    unittest.main()



'''
22/04/2020

713. Subarray Product Less Than K - Medium

Tag: Array, Two Pointers

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.

'''

from typing import List
import math
# Solution
class Solution1:
    '''
    Binary search on Logarithms
    Time complexity : O(nlogN)
    Space complexity : O(n)
    '''
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums or k == 0:
            return 0
        
        k = math.log(k)
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1]+math.log(x))
        
        def find_right(nums, target):
            l, r = 0, len(nums)-1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r
        
        ans = 0
        
        for idx, x in enumerate(prefix):
            # k = target - x
            end = find_right(prefix, k+x-1e-9)
            if end != -1:
                ans += end - idx
        
        return ans


class Solution2:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        Sliding windows
        Time: O(N)
        Space: O(1)
        '''
        if not nums or k <= 1:
            return 0
        
        prod = 1
        res = 0
        left = 0
        for right, x in enumerate(nums):
            prod *= x
            while prod >= k:
                prod //= nums[left]
                left += 1
            res += right-left+1
        
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
            func = Sol.numSubarrayProductLessThanK
            self.assertEqual(func([10,5,2,6], 100), 8)
            self.assertEqual(func([1,2,3], 0), 0)
            self.assertEqual(func([1,1,1], 1), 0)

if __name__ == '__main__':
    unittest.main()
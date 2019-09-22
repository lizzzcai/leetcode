"""
21/09/2019
41. First Missing Positive - Hard
Tag: Array, in-place

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1

"""

from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        assume we have k positive integer in the list, k <=len(nums)
        if we have k positive number, the first missing positive number must with [1, k+1]
        
        1. partition the nums,  to move all k number of positive number to idx [0, k-1], 0 and negative number to [k,n-1]
        2. iterate through nums[0, k-1], assign nums[nums[idx]-1] = -nums[nums[idx]-1] if nums[idx] <= k
        
        iterate through nums[0, k-1] again, find the first nums[idx] is positive, then idx + 1 is the first missing positive
        
        Time: O(n)
        Space: O(1)
        
        """
        
        def partition(nums):
            """
            in-place partition, swap all the positive number to the left
            return the number of positive number, k
            """
            k = 0
            for i in range(len(nums)):
                if nums[i]  > 0:
                    nums[k], nums[i] = nums[i], nums[k]
                    k += 1
            return k
        
        
        # apply partition on nums, k is the total number of positive number
        k = partition(nums)
        print("k:", k)
        print("nums of partition: ",nums)
        # iterate through the first k
        for i in range(k):
            val = nums[i] if nums[i] > 0 else -nums[i]
            # for val in range[1,k]
            # assign nums[val-1] to negative if val is positive, it means val appear at val-1 location
            if val <= k:
                nums[val-1] = -nums[val-1] if nums[val-1] > 0 else nums[val-1]
        
        print("nums after process:", nums)
        # itereate through first k agian, find the first positive value
        for i in range(k):
            if nums[i] > 0:
                return i+1
        return k+1


class Solution1:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        assume we have k positive integer in the list, k <=len(nums)
        if we have k positive number, the first missing positive number must with [1, k+1]
        
        1. partition the nums,  to move all k number of positive number to idx [0, k-1], 0 and negative number to [k,n-1]
        1. for num <=0 or num > n+1, assign as n+1
        2. iterate through nums, assign nums[nums[idx]-1] = -nums[nums[idx]-1] if nums[idx]-1 < n
        
        iterate through nums[0, k-1] again, find the first nums[idx] is positive, then idx + 1 is the first missing positive
        
        Time: O(n)
        Space: O(1)
        
        """

        # first positive value must within [1, n+1]
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n+1
        
        # nums as idx and assgin the relative value to negative to indicate it's appear
        for i in range(n):
            idx = abs(nums[i]) - 1
            # for valid idx
            if idx < n:
                nums[idx] = -abs(nums[idx])
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n+1
             

# Unit Test
import unittest
class firstMissingPositiveCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_firstMissingPositive(self):
        func = Solution().firstMissingPositive

        self.assertEqual(func([]), 1)
        self.assertEqual(func([1,2,0]), 3)
        self.assertEqual(func([3,4,-1,1]), 2)
        self.assertEqual(func([7,8,9,11,12]), 1)



if __name__ == '__main__':
    unittest.main()



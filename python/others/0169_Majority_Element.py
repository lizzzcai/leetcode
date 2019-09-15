"""
15/09/2019
160. Majority Element - Easy
Tag: Other

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2



"""

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
        
    def majorityElement_sort(self, nums):
        nums.sort()
        return nums[len(nums)//2]

# Unit Test
import unittest
class majorityElementCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_majorityElement(self):
        func = Solution().majorityElement
 

        self.assertEqual(func([3,2,3]), 3)
        self.assertEqual(func([2,2,1,1,1,2,2]), 2)









if __name__ == '__main__':
    unittest.main()



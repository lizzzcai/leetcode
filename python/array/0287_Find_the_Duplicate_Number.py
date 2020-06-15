"""
21/09/2019
287. Find the Duplicate Number - Medium
Tag: Array, set, link list

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

"""

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set()
        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)
        
class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        runner1 = nums[0]
        runner2 = nums[0]
        while True:
            runner1 = nums[runner1]
            runner2 = nums[nums[runner2]] # move 2 steps
            if runner1 == runner2:
                break
        
        # find the entrance of the cycle
        ptr1 = nums[0]
        ptr2 = runner1
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        
        return ptr1

class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        
        l, h = 1, len(nums)-1
        
        while l <= h:
            mid = (l+h)//2
            count = 0
            for x in nums:
                if x <= mid:
                    count += 1
            if count <= mid:
                l = mid + 1
            else:
                h = mid-1
        
        return l


# Unit Test
import unittest
class findDuplicateCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_findDuplicate(self):
        func = Solution().findDuplicate
        self.assertEqual(func([]), 0)
        self.assertEqual(func([1,3,4,2, 2]), 2)
        self.assertEqual(func([3,1,3,4,2]), 3)








if __name__ == '__main__':
    unittest.main()



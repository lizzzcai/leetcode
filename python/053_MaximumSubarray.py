'''

53. Maximum Subarray - Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''

# Solution
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        hmap = {} # store the difference between target and selected num.
        res = [] # res list
        for i in range(n):
            # check if the num in the hashmap.
            if nums[i] in hmap:
                # if in the map, means previous there is a value which
                # meets the requirement (previous + current = target)
                
                res.append(hmap[nums[i]]) # the previous value should be placed at the first
                res.append(i)
                return res
            else:
                # if not in the map, add the future value which meet 
                # the requirement with this current value in the map
                # for retrieve in the next.
                # {(target - current) : index of current num}
                hmap[target - nums[i]] = i

# Unit Test
import unittest
class TwoSumCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_twoSum(self):
        func = Solution().twoSum
        self.assertEqual(func([2, 7, 11, 15], 9), [0, 1])

if __name__ == '__main__':
    unittest.main()
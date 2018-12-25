'''
26/12/2018

Tag: Array, Dynamic Programing, Divide and Conquer

53. Maximum Subarray - Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

'''

class Solution1(object):
    """
    Solution 1, dynamic programing 
    O(n)
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # init the first value of the list
        # as result and current sum
        res, currSum = nums[0], nums[0]
        
        for idx in range(1, len(nums)): # skip the first value
            # Because it is the contiguous subarray (containing at least one number),
            # if the value of the nums in the current idx larger than the previous sum,
            # it means the current value can at least represent the previous sum, 
            # so it can be a single value contigous subarray.
            currSum = max(currSum + nums[idx], nums[idx])
            # during each iteration, find the max current sum as the result.
            res = max(res, currSum)
        return res


class Solution2:
    """
    Solution 2, divide and conquer 

    Time Complexity: O(logn). 

    Space Complexity: 
    '''
    """
    def DivideAndConquer(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """
        if left > right:
            return -2147483647
        
        # get the mid index
        mid = (left + right) // 2
        
        # a array is dvided in to left, mid, right 3 parts.
        # will calculate the max of sum start from mid to both sides.
        # compare the result of sum of right, left and the sum across the mid.
        
        # get the max sum for both left and right sides
        # mid value is skipped, will add back at the end.
        
        # for left side
        maxSum_left = sumVal = 0
        for i in range(mid-1, left-1, -1): # -1 to include the left idx
            sumVal += nums[i]
            maxSum_left = max(maxSum_left, sumVal)

        # for right side
        maxSum_right = sumVal = 0
        for i in range(mid+1, right+1, 1): # +1 to include the right idx
            sumVal += nums[i]
            maxSum_right = max(maxSum_right, sumVal)
        
        # divide and conquer on both left and right sides
        # not include the mid value
        # left: [left, mid)
        leftAns = self.DivideAndConquer(nums, left, mid-1)
        # right: (mid, right]
        rightAns = self.DivideAndConquer(nums, mid+1, right)
        
        # return the max result between, leftAns, rightAns,
        # and the value across left and right
        return max(max(leftAns, rightAns), maxSum_left + nums[mid] + maxSum_right)

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.DivideAndConquer(nums, 0, len(nums)-1)

# Unit Test
import unittest
class maxSubArrayCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_maxSubArray(self):
        func = Solution1().maxSubArray
        self.assertEqual(func([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(func([1]), 1)
        self.assertEqual(func([-1,-2]), -1)

        func = Solution2().maxSubArray
        self.assertEqual(func([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(func([1]), 1)
        self.assertEqual(func([-1,-2]), -1)

if __name__ == '__main__':
    unittest.main()
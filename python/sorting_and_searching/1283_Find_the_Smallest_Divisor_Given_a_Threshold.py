'''
19/04/2020

Tag: Binary Search

1283. Find the Smallest Divisor Given a Threshold - Medium


Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide all the array by it and sum the result of the division. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.

 

Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
Example 2:

Input: nums = [2,3,5,7,11], threshold = 11
Output: 3
Example 3:

Input: nums = [19], threshold = 5
Output: 4
 

Constraints:

1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6

'''

from typing import List
import math
class Solution1:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        _sum = sum(nums)
        left = math.ceil(_sum / threshold)
        right = left * 3
        
        while left <= right:
            mid = (left + right) // 2
            divisor = sum(math.ceil(x/mid) for x in nums)
            if divisor <= threshold: # lower the mid
                right = mid - 1
            else:
                left = mid + 1
        
        return left

class Solution2:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        '''
        Time O(NlogM), M = max(A)
        Space O(1)
        '''
        left, right = 1, max(nums)
        
        while left <= right:
            mid = (left + right) // 2
            # (x + y - 1) // y : rounded-up version of x/y
            # divisor = sum(math.ceil(x/mid) for x in nums)
            divisor = sum((x+mid-1) // mid for x in nums)
            if divisor > threshold: # the divisor is too small, increase the divisor
                left = mid + 1
            else: # the divisor is big enough
                right = mid - 1
        
        return left

# Unit Test
import unittest
class smallestDivisorCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.smallestDivisor
            self.assertEqual(func([1,2,5,9], 6), 5)
            self.assertEqual(func([2,3,5,7,11], 11), 3)
            self.assertEqual(func([19], 5), 4)
            self.assertEqual(func([1,2,3], 1000000), 1)
if __name__ == '__main__':
    unittest.main()
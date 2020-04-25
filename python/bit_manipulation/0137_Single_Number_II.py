'''
25/04/2020

137. Single Number II - Medium

Tag: Bit Manipulation

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(1, len(nums)-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]
    
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        https://leetcode.com/problems/single-number-ii/discuss/43385/Python-bitwise-solution
        '''
        def convert(x):
            if x >= 2**31:
                x -= 2**32
            return x
    
        ans = 0
        for i in range(32):
            count = 0
            for x in nums:
                if (x>>i) & 1:
                    count += 1
            ans |= (count % 3) << i
        
        return convert(ans)


class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        https://leetcode.com/problems/single-number-ii/discuss/43332/My-own-explanation-of-bit-manipulation-method-might-be-easier-to-understand
        '''
        ones, twos = 0, 0
        for x in nums:
            ones = (~twos)&(ones^x)
            twos = (~ones)&(twos^x)
        
        # at the end, if apear ONCE, ones bit will be 1
        return ones

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2(), Solution3()]:
            func = Sol.singleNumber
            self.assertEqual(func([2,2,3,2]), 3)
            self.assertEqual(func([0,1,0,1,0,1,99]), 99)
            self.assertEqual(func([1]), 1)

if __name__ == '__main__':
    unittest.main()
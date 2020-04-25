'''
25/04/2020

260. Single Number III - Medium

Tag: Bit Manipulation

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''

from typing import List


# Solution
class Solution1:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''
        Time O(n)
        Space O(1)
        
        https://leetcode.com/problems/single-number-iii/discuss/68900/Accepted-C%2B%2BJava-O(n)-time-O(1)-space-Easy-Solution-with-Detail-Explanations
        
        Let a and b be the two unique numbers
        XORing all numbers gets you (a xor b)
        (a xor b) must be non-zero otherwise they are equal
        If bit_i in (a xor b) is 1, bit_i at a and b are different.
        Find bit_i using the low bit formula m & -m
        Partition the numbers into two groups: one group with bit_i == 1 and the other group with bit_i == 0.
        a is in one group and b is in the other.
        a is the only single number in its group.
        b is also the only single number in its group.
        XORing all numbers in a's group to get a
        XORing all numbers in b's group to get b
        Alternatively, XOR (a xor b) with a gets you b.
        
        '''
        # to get a ^ b
        xor = 0
        for x in nums:
            xor ^= x
            
        # find the last bit that they are different by diff &= ~(diff - 1)
        
        # diff &= -diff : ~(diff - 1) = - (diff - 1) - 1 = -diff
        
        last_bit = xor & ~(xor-1)
        # so that we are different in this bit
        
        # divide a and b into two group by this bit
        # group = [x for x in nums if x & last_bit != 0]
        
        # so in group, all number apprear twice except a,  xor the new group to get a
        # a = 0
        # for x in group:
        #    a ^= x
        a = 0
        for x in nums:
            if x & last_bit:
                a ^= x
        
        
        # a xor (a^b) to get b
        b = a ^ xor
        
        return[a, b]
        


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.singleNumber
            self.assertEqual(set(func([1,2,1,3,2,5])), set([3,5]))


if __name__ == '__main__':
    unittest.main()
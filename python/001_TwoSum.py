'''
26/12/2018

Tag: Hash Table

1. Two Sum - Easy


Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

# Solution
class Solution:
    '''
    Time complexity : O(n). We traverse the list containing nn elements only once. Each look up in the table costs only O(1) time.
    Space complexity : O(n). The extra space required depends on the number of items stored in the hash table, which stores exactly nn elements.
    '''
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                # if in the map, means previous there is a value which
                # meets the requirement (previous + current = target)
                # return [previous_idx, current_idx]
                # the previous value should be placed at the first
                return [hashmap[complement], i]
            else:
                # if not in the map, add this current value which meet 
                # the requirement with the future value in the map
                # for retrieve in the next.
                # {current : index of current num}
                hashmap[nums[i]] = i
        raise ValueError("No two sum solution")

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
        self.assertEqual(func([2, 7, 15, 16], 17), [0, 2])

if __name__ == '__main__':
    unittest.main()
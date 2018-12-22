'''

1. Two Sum - Easy

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

# Solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
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
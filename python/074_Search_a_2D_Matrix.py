'''
19/02/2019

74. Search a 2D Matrix - Medium

Tag: Array, Binary

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

'''

# Solution
class Solution:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
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
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().twoSum
        self.assertEqual(func([2, 7, 11, 15], 9), [0, 1])

if __name__ == '__main__':
    unittest.main()
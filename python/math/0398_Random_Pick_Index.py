'''
08/02/2020

398. Random Pick Index - Medium

Tag: Reservoir Sampling

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);

'''

from typing import List
# Solution
from random import randrange
class Solution:
    '''
    Reservoir Sampling Prove 
    https://www.youtube.com/watch?v=Ybra0uGEkpM
    '''
    def __init__(self, nums: List[int]):
        self.arr = nums
        

    def pick(self, target: int) -> int:
        i = 0
        res = None
        for idx, num in enumerate(self.arr):
            if num != target:
                continue
            i += 1
            if randrange(1, i+1) == i:
                res = idx
        
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        nums = [1,2,3,3,3]
        target = 3
        obj = Solution(nums)
        param_1 = obj.pick(target)

        #self.assertEqual(param_1, [0, 1])
        self.assertIn(param_1, [2, 3, 4])

if __name__ == '__main__':
    unittest.main()
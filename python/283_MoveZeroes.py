'''
05/02/2019

283. Move Zeroes - Easy

Tag: Array, two pointer

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''


class Solution:
    '''
    Two pointer

    All elements before the slow pointer (lastNonZeroFoundAt) are non-zeroes.

    All elements between the current and slow pointer are zeroes.

    Therefore, when we encounter a non-zero element, we need to swap elements pointed by current and slow pointer, 
    then advance both pointers. If it's zero element, we just advance current pointer.

    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNoneZero = 0
        for curr in range(len(nums)):
            if nums[curr] != 0:
                # swap the value
                nums[lastNoneZero], nums[curr] = nums[curr], nums[lastNoneZero]
                lastNoneZero += 1
        
        return nums
                   

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().moveZeroes
        self.assertEqual(func([0,1,0,3,12]), [1,3,12,0,0])
        self.assertEqual(func([0,0,0,1]), [1,0,0,0])
        self.assertEqual(func([1]), [1])



if __name__ == '__main__':
    unittest.main()
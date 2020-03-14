'''
14/03/2020

315. Count of Smaller Numbers After Self - Hard

Tag: Binary Search, Divide and Conquer, Sort, Binary Indexed Tree, Segment Tree

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

'''

from typing import List
# SDivide and Conquer olution
class Solution1:
    def countSmaller(self, nums: List[int]) -> List[int]:
        '''
        https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution

        divide and conquer solution
        as we do the merge sort, we will swap the the number from left to right, base on that we can calculate the number greater/smaller than the mid

        '''

        def divide(tuple_nums):
            mid = len(tuple_nums) // 2
            if mid: # len(tuple_nums) > 1
                left = divide(tuple_nums[:mid])
                right = divide(tuple_nums[mid:])
                return conquer(left, right)
            else: # len(tuple_nums) == 1
                return tuple_nums

        def conquer(left, right):
            sort = [] # descent
            i, j = 0, 0
            while i < len(left) and j < len(right):
                # append the larger value
                if left[i][0] > right[j][0]:
                    sort.append(left[i])
                    # as left and right are sorted
                    # if left[i][0] larger than right[j][0],
                    # left[i] > right[j:], so add the count len(right)-j into indx left[i][1]
                    res[left[i][1]] += len(right) - j
                    i += 1
                else:
                    sort.append(right[j])
                    j += 1
            
            # add the rest 
            if i < len(left):
                sort.extend(left[i:])
            if j < len(right):
                sort.extend(right[j:])
            
            return sort

        if not nums:
            return []

        res = [0] * len(nums)
        tuple_nums = [(num, idx) for idx, num in enumerate(nums)]
        divide(tuple_nums)
        return res      
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.countSmaller
            self.assertEqual(func([]), [])
            self.assertEqual(func([1]), [0])
            self.assertEqual(func([1,1]), [0,0])
            self.assertEqual(func([5,2,6,1]), [2,1,1,0])
            self.assertEqual(func([5,2,6,1,5,3,2,7,8,10]), [4,1,4,0,2,1,0,0,0,0])





if __name__ == '__main__':
    unittest.main()
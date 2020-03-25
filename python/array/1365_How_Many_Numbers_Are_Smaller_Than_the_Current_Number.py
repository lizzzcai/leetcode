'''
14/03/2020

1365. How Many Numbers Are Smaller Than the Current Number - Easy

Tag: Array, Hash Table

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

 

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]
 

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100


'''

from typing import List
# Solution
class Solution1:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
        Time: O(NlogN)
        Space: O(N)

        '''
        def find_left(l, r, nums, target):
            # binary search
            while l <= r:
                mid = l + (r-l) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            # return the first element meet the target        
            return l
            
        
        n = len(nums)
        sorted_nums = sorted(nums)
        res = []
        for num in nums:
            res.append(find_left(0, n-1, sorted_nums, num))
        
        return res

class Solution2:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
        hashmap
        Time: O(NlogN)
        Space: O(1) (up to 101 numbers in indices)

        '''
        res = []
        hmap = {}
        n = len(nums)
        for idx, num in enumerate(sorted(nums, reverse=True)):
            hmap[num] = idx
            
        for num in nums:
            res.append(n-1 - hmap[num])
        
        return res

class Solution3:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
        Time: O(N)
        Space: O(1) (range is 1 ~ 100)
        '''
        count = [0] * 102
        for num in nums:
            count[num+1] += 1
        for i in range(1, 102):
            count[i] += count[i-1]
        
        res = [count[num] for num in nums]
        return res
        
class Solution4:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        res = []
        sorted_nums = sorted(nums)
        hmap = {}
        for idx, num in enumerate(sorted_nums):
            if num not in hmap:
                hmap[num] = idx
        
        for num in nums:
            res.append(hmap[num])
            
        return res

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(), Solution3(), Solution4()]:
            func = Sol.smallerNumbersThanCurrent
            self.assertEqual(func([8,1,2,2,3]), [4,0,1,1,3])
            self.assertEqual(func([6,5,4,8]), [2,1,0,3])
            self.assertEqual(func([7,7,7,7]), [0,0,0,0])



if __name__ == '__main__':
    unittest.main()
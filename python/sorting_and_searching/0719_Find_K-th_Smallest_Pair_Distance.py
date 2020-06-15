'''
14/03/2020

719. Find K-th Smallest Pair Distance - Hard

Tag: Array, Binary Search, Heap

Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.

'''

from typing import List
# Solution
class Solution1:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        '''
        https://leetcode.com/problems/find-k-th-smallest-pair-distance/discuss/196304/Verbosely-commented-Python-Approach-3-with-example-walkthrough
        https://leetcode.com/problems/find-k-th-smallest-pair-distance/solution/
        
        '''
        # if there are k or more pairs equal or smaller than dist, in sorted nums
        def euqal_greater_than_k(guess_dist):
            left = 0
            count = 0
            for right, num in enumerate(nums):
                # to find the range that distance <= guess distance
                # left will be < right
                while left < right and num - nums[left] > guess_dist:
                    left += 1
                count += right - left
            
            return count >= k
        
        # sort the nums
        nums.sort()
        # nums[-1] - nums[0] is the max distance from the nums
        l, r = 0, nums[-1] - nums[0]
        
        while l <= r:
            mid = (l+r) // 2
            # if equal or more than k pairs' distance equal or smaller than mid
            if euqal_greater_than_k(mid):
                r = mid - 1
            else:
                l = mid + 1
        # first vlaue meet the target
        return l



class Solution2:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        '''
        https://leetcode.com/problems/find-k-th-smallest-pair-distance/discuss/196304/Verbosely-commented-Python-Approach-3-with-example-walkthrough
        https://leetcode.com/problems/find-k-th-smallest-pair-distance/solution/
        
        
        https://leetcode.com/problems/find-k-th-smallest-pair-distance/discuss/109082/Approach-the-problem-using-the-%22trial-and-error%22-algorithm
        
        '''
        
        nums.sort()
        n = len(nums)
        l, h = 0, nums[-1]-nums[0]
        
        while l <= h:
            mid = (l+h) // 2
            count = 0
            i = 0
            for j in range(n):
                while i < j and nums[j]-nums[i] > mid:
                    i+=1
                if j > i:
                    count += j-i
            
            if count < k:
                l = mid + 1
            else:
                h = mid - 1
        
        return l
                

        
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.smallestDistancePair
            self.assertEqual(func([1,3,1], 1), 0)
            self.assertEqual(func([62,100,4], 2), 58)




if __name__ == '__main__':
    unittest.main()
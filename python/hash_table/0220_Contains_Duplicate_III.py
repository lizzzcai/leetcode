'''
03/09/2020

220. Contains Duplicate III - Medium

Tag: Hash Table, Sort, Ordered Map

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
'''

from typing import List
# Solution
class Solution1:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        '''
        https://leetcode.com/problems/contains-duplicate-iii/discuss/61645/AC-O(N)-solution-in-Java-using-buckets-with-explanation
        time: O(n)
        '''
        if k < 1 or t < 0:
            return False
        hmap = dict()
        MIN = -2**31
        for idx, x in enumerate(nums):
            new = x - MIN
            bucket = new // (t+1)
            if bucket in hmap \
            or (bucket-1 in hmap and new-hmap[bucket-1]<=t) \
            or (bucket+1 in hmap and hmap[bucket+1]-new<=t):
                return True
            # if size larger than k
            if len(hmap) >= k:
                last_bucket = (nums[idx-k]- MIN) // (t+1)
                hmap.pop(last_bucket, None)
            
            hmap[bucket] = new
            
        return False
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.containsNearbyAlmostDuplicate
            self.assertEqual(func([1,2,3,1],3,0), True)
            self.assertEqual(func([1,0,1,1],1,2), True)
            self.assertEqual(func([1,5,9,1,5,9],2,3), False)



if __name__ == '__main__':
    unittest.main()
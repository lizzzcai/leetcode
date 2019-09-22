"""
21/09/2019
128. Longest Consecutive Sequence - Hard
Tag: Array

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

"""

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time: O(nlgn)
        Space: O(1), in-place sort
        """
        if not nums:
            return 0
        nums.sort()
        res = 1
        n = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    n+= 1
                else:
                    n = 1
            res = max(res, n)
        
        return res

class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        use set to store and have O(1) look up
        1. create a set, init res = 0, if no num, return 0

        2. for each num in num-set, if num-1 not in num-set,
            start from new cnt, curr = num, n = 1

            for curr + 1, if in num_set, curr += 1, n += 1
            else, break and compare with res. res = max(res, n)
        
        3. return res

        Time: O(n)
        Space: O(n)
        """
        
        res = 0
        num_set = set(nums)
        
        for num in num_set:
            if num-1 not in num_set:
                curr_num = num
                n = 1
                
                while curr_num + 1 in num_set:
                    curr_num += 1
                    n += 1
                
                res = max(res, n)
        
        return res
        

# Unit Test
import unittest
class longestConsecutiveCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_longestConsecutive(self):
        func = Solution().longestConsecutive

        self.assertEqual(func([]), 0)
        self.assertEqual(func([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(func([0, -1]), 2)
        self.assertEqual(func([1,2,0,1]), 3)
        self.assertEqual(func([9,1,4,7,3,-1,0,5,8,-1,6]), 7)









if __name__ == '__main__':
    unittest.main()



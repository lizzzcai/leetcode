'''
26/04/2020

45. Jump Game II - Hard

Tag: Array, Greedy

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
'''

from typing import List
# Solution
class Solution1:
    def jump(self, nums: List[int]) -> int:
        '''
        
        Greedy TLE
        https://leetcode.com/problems/jump-game-ii/discuss/18028/O(n)-BFS-solution
        O(N^2)
        O(1)
        
        '''
        steps = 0
        curr_pos = len(nums)-1
        while curr_pos != 0:
            for i in range(0, curr_pos):
                if i+nums[i] >= curr_pos:
                    curr_pos = i
                    steps += 1
                    break
        
        return steps

class Solution2:
    def jump(self, nums: List[int]) -> int:
        '''
        
        BFS
        https://leetcode.com/problems/jump-game-ii/discuss/18014/Concise-O(n)-one-loop-JAVA-solution-based-on-Greedy
        O(N)
        O(1)
        
        '''
        steps = 0
        curr_end = 0
        curr_farthest = 0

        for i in range(0, len(nums)-1):
            curr_farthest = max(curr_farthest, i+nums[i])
            if i == curr_end:
                curr_end = curr_farthest
                steps += 1
            
            if curr_end >= len(nums)-1:
                break
        
        return steps


class Solution3:
    def jump(self, nums: List[int]) -> int:
        '''
        
        Greedy
        https://leetcode.com/problems/jump-game-ii/discuss/170518/8-Lines-in-Python!-Easiest-Solution!
        O(N)
        O(1)
        
        '''
        if len(nums) <= 1: return 0
        steps = 1
        l, r = 0, nums[0]
        while r < len(nums)-1:
            steps += 1
            nxt = max(i+nums[i] for i in range(l, r+1))
            l, r = r+1, nxt

        return steps

import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(), Solution3()]:
            func = Sol.jump
            self.assertEqual(func([2,3,1,1,4]), 2)
            self.assertEqual(func([2,3,1,2,3,4,2,1,1,3,2,1,4]), 5)
            self.assertEqual(func([2,1]), 1)
            self.assertEqual(func([0]), 0)

if __name__ == '__main__':
    unittest.main()
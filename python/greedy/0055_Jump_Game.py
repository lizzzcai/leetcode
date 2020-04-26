'''
26/04/2020

55. Jump Game - Medium

Tag: Array, Greedy

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

'''

from typing import List
# Solution
class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Dynamic Programming Top-down
        Time O(n^2) TLE
        Space: O(n)
        '''
        n = len(nums)
        memo = [0]*n
        
        memo[n-1] = 1 # 1 good, 0 unknown, -1 bad
        
        def canJumpFromPosition(pos, nums, memo):
            if memo[pos] == 1:
                return True
            if memo[pos] == -1:
                return False

            
            furthestJump = min(pos+nums[pos], n-1)
            for i in range(pos+1, furthestJump+1):
                if canJumpFromPosition(i, nums, memo):
                    memo[pos] = 1
                    return True
            
            memo[pos] = -1
            return False
        
        return canJumpFromPosition(0, nums, memo)


class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Dynamic Programming Bottom-up
        Time O(n^2) TLE
        Space: O(n) 
        '''
        n = len(nums)
        memo = [0]*n
        
        memo[n-1] = 1 # 1 good, 0 unknown, -1 bad
        
        for i in range(n-2, -1, -1):
            furthestJump = min(i+nums[i], n-1)
            for j in range(i+1, furthestJump+1):
                if memo[j] == 1:
                    memo[i] = 1
                    break
        
        return memo[0] == 1

class Solution3:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Greedy
        Time O(n)
        Space: O(1)
        '''
        
        furthestJump = nums[0]
        for i in range(1, len(nums)):
            if i > furthestJump:
                return False
            furthestJump = max(furthestJump, nums[i]+i)
        
        return True
        
class Solution4:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Greedy
        Time O(n)
        Space: O(1)
        '''
        
        furthestJump = 0
        for i, x in enumerate(nums):
            if i > furthestJump:
                return False
            furthestJump = max(furthestJump, i+x)
        
        return True


class Solution5:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Greedy
        Time O(n)
        Space: O(1)
        '''
        
        lastPos = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i] >= lastPos:
                lastPos = i
        
        return lastPos == 0

import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(),Solution3(),Solution4(),Solution5()]:
            func = Sol.canJump
            self.assertEqual(func([2,3,1,1,4]), True)
            self.assertEqual(func([3,2,1,0,4]), False)

if __name__ == '__main__':
    unittest.main()
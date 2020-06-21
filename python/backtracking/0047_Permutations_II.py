'''
21/06/2020

47. Permutations II - Medium

Tag: Backtracking

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

'''
import collections
from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(track, counter):
            if len(track) == len(nums):
                res.append(track[:])
            
            for x in counter: # avoid duplicates
                if counter[x] > 0:
                    counter[x] -= 1
                    backtrack(track+[x], counter)
                    counter[x] += 1
        
        res = []
        backtrack([], collections.Counter(nums))
        return res

class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        https://leetcode.com/problems/permutations-ii/discuss/18594/Really-easy-Java-solution-much-easier-than-the-solutions-with-very-high-vote
        
        if (i > 0 && nums[i] == nums[i - 1] && !use[i - 1]) continue; means, in other words, if previous identical number is used, then use the current number.
        
        The difficulty is to handle the duplicates.
        With inputs as [1a, 1b, 2a],
        If we don't handle the duplicates, the results would be: [1a, 1b, 2a], [1b, 1a, 2a]...,
        so we must make sure 1a goes before 1b to avoid duplicates
        By using nums[i-1]==nums[i] && !used[i-1], we can make sure that 1b cannot be choosed before 1a
        '''
        def backtrack(track, nums, visited):
            if len(track) == len(nums):
                res.append(track[:])
            
            for i in range(len(nums)):
                if visited[i] or (i > 0 and nums[i-1] == nums[i] and not visited[i-1]):
                    continue
                visited[i] = True
                backtrack(track+[nums[i]], nums, visited)
                visited[i] = False
        
        res = []
        nums.sort()
        visited = [False]*len(nums)
        backtrack([], nums, visited)
        return res

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.permuteUnique
            self.assertEqual(func([1,1,2]), [[1,1,2],[1,2,1],[2,1,1]])

if __name__ == '__main__':
    unittest.main()
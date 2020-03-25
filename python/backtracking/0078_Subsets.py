'''
14/03/2020

78. Subsets - Medium

Tag: Backtracking

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''

from typing import List
# Solution
class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(curr, left, n, track):
            
            res.append(track.copy())
            if left == 0:
                return
            
            for i in range(curr, n):
                track.append(nums[i])
                backtrack(i+1, left-1, n, track)
                track.pop()
            
        
        n = len(nums)
        res = []
        backtrack(0, n, n, [])
        
        return res

class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(curr, n, track):
            
            res.append(track.copy())

            
            for i in range(curr, n):
                track.append(nums[i])
                backtrack(i+1, n, track)
                # backtrack(i+1, n, track+[nums[i]])
                track.pop()
            
        
        n = len(nums)
        res = []
        backtrack(0, n, [])
        
        return res

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.subsets
            out = [
                [3],
                [1],
                [2],
                [1,2,3],
                [1,3],
                [2,3],
                [1,2],
                []
            ]
            self.assertEqual(set(tuple(x) for x in func([1,2,3])), set(tuple(x) for x in out))

if __name__ == '__main__':
    unittest.main()
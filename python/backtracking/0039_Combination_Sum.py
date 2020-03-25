'''
25/03/2020

39. Combination Sum - Medium

Tag: Backtracking

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''

from typing import List
# Solution
class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(curr, left, track):
            
            if left == 0:
                res.append(track.copy())
                return
            
            for i in range(curr, len(candidates)):
                # if num > left, exceeded the sum with candidate[i]
                if candidates[i] <= left:
                    #track.append(candidates[i])
                    backtrack(i, left - candidates[i], track+[candidates[i]])
                    #track.pop()
        
        candidates.sort()
        res = []
        backtrack(0, target, [])
        return res


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(curr, left, track):
            
            if left == 0:
                res.append(track.copy())
                return
            
            for i in range(curr, len(candidates)):
                # if num > left, exceeded the sum with candidate[i]
                if candidates[i] > left:
                    break
                track.append(candidates[i])
                backtrack(i, left - candidates[i], track)
                track.pop()
        
        candidates.sort()
        res = []
        backtrack(0, target, [])
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
            func = Sol.combinationSum
            self.assertEqual(set(tuple(x) for x in func([2,3,6,7], 7)), set(tuple(x) for x in [[7], [2,2,3]]))
            self.assertEqual(set(tuple(x) for x in func([2,3,5], 8)), set(tuple(x) for x in [[2,2,2,2], [2,3,3], [3,5]]))


if __name__ == '__main__':
    unittest.main()
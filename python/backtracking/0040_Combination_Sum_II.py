'''
25/03/2020

40. Combination Sum II - Medium

Tag: Backtracking

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

'''

from typing import List
class Solution1:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(n, curr, left, track):
            if left == 0:
                res.append(track[:])
            
            for i in range(curr, n):
                if candidates[i] > left:
                    break
                # we want to start detecting dupe in the second round of looping, after previous number(starting from first) has already been processed(i>cur)
                if i > curr and candidates[i] == candidates[i-1]:
                    continue
                track.append(candidates[i])
                backtrack(n, i+1, left-candidates[i], track)
                track.pop()
                
        
        n = len(candidates)
        candidates.sort()
        res = []
        backtrack(n, 0, target, [])
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
            func = Sol.combinationSum2
            self.assertEqual(set(tuple(x) for x in func([10,1,2,7,6,1,5], 8)), set(tuple(x) for x in [[1, 7],[1, 2, 5],[2, 6],[1, 1, 6]]))
            self.assertEqual(set(tuple(x) for x in func([2,5,2,1,2], 5)), set(tuple(x) for x in [[1,2,2],[5]]))


if __name__ == '__main__':
    unittest.main()
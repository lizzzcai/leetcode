'''
25/03/2020

77. Combinations - Medium

Tag: Backtracking

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

from typing import List
# Solution
class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(nums, track):
            if len(track) == k:
                res.append(track.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in track:
                    track.append(nums[i])
                    backtrack(nums[i+1:], track)
                    track.pop()
        
        res = []
        nums = [i for i in range(1, n+1)]
        backtrack(nums, [])
        
        return res


class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(nums, track, curr):
            if len(track) == k:
                res.append(track.copy())
                return
            
            for i in range(curr, len(nums)):
                if nums[i] not in track:
                    track.append(nums[i])
                    backtrack(nums, track, i+1)
                    track.pop()
        
        if k == 0:
            return [[]]
        
        res = []
        nums = [i for i in range(1, n+1)]
        backtrack(nums, [], 0)
        
        return res
        

class Solution3:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(n, k, curr, track):
            if k == 0:
                res.append(track.copy())
                return
            
            for i in range(curr, n+1):
                if i not in track:
                    track.append(i)
                    backtrack(n, k-1, i+1, track)
                    track.pop()
        
        if k == 0:
            return [[]]
        
        res = []
        backtrack(n, k, 1, [])
        return res
        


class Solution4:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(n, k, curr, track):
            if k == 0:
                res.append(track.copy())
                return
            # n+1 -k + 1 to purage 
            # as when the rest is not enough for k, there is no need to keep search.
            # you should not continue exploring (recursing) when you know that there won't be enough numbers left until n to fill the needed k slots. If n = 10, k = 5, and you're in the outermost level of recursion, you choose only i = 1...6 , because if you pick i=7 and go into backTracking() you only have 8,9,10 to pick from, so at most you will get [7,8,9,10]... but we need 5 elements!
            for i in range(curr, n-k+2):
                track.append(i)
                backtrack(n, k-1, i+1, track)
                track.pop()
        
        if k == 0:
            return [[]]
        
        res = []
        backtrack(n, k, 1, [])

        return res
        


class Solution5:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        https://leetcode.com/problems/combinations/discuss/27002/Backtracking-Solution-Java
        '''
        def backtrack(fm, to, kleft, track):
            if kleft == 0:
                res.append(track.copy())
                return
            # n+1 -k + 1 to purage 
            # as when the rest is not enough for k, there is no need to keep search.
            
            '''
            you should not continue exploring (recursing) when you know that there won't be enough numbers left until n to fill the needed k slots. If n = 10, k = 5, and you're in the outermost level of recursion, you choose only i = 1...6 , because if you pick i=7 and go into backTracking() you only have 8,9,10 to pick from, so at most you will get [7,8,9,10]... but we need 5 elements!
            
            '''
            
            for i in range(fm, to+1):
                track.append(i)
                backtrack(i+1, to+1, kleft-1, track)
                track.pop()
        
        if k == 0:
            return [[]]
        
        res = []
        # valid range [1, n-k+1]
        backtrack(1, n-k+1, k, [])
        
        return res
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(), Solution3(), Solution4(), Solution5()]:
            func = Sol.combine
            out = [
                [2,4],
                [3,4],
                [2,3],
                [1,2],
                [1,3],
                [1,4],
            ]
            self.assertEqual(set(tuple(x) for x in func(4, 2)), set(tuple(x) for x in out))

if __name__ == '__main__':
    unittest.main()
'''
14/03/2020

46. Permutations - Medium

Tag: Backtracking

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''

from typing import List
# Solution
class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        https://en.wikipedia.org/wiki/Permutation#k-permutations_of_n
        Time: O(N!)
        '''
        def backtrack(nums, track):
            if len(track) == len(nums):
                res.append(track.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in track:
                    track.append(nums[i])
                    backtrack(nums, track)
                    track.pop()
            
        res = []
        backtrack(nums, [])
        return res

class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Backtracking
        https://blog.csdn.net/zxzxzx0119/article/details/81452269
        Time: O(N!)
        '''
        def backtrack(nums, curr):
            if curr == len(nums):
                res.append(nums.copy())
                return
            
            # selection list
            # when curr == idx, the curr is fixed.
            for idx in range(curr, len(nums)):
                # swap
                nums[curr], nums[idx] = nums[idx], nums[curr]
                backtrack(nums, curr + 1)
                # undo the swap
                nums[curr], nums[idx] = nums[idx], nums[curr]
            
        res = []
        backtrack(nums, 0)
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
            func = Sol.permute
            out = [
                [1,2,3],
                [1,3,2],
                [2,1,3],
                [2,3,1],
                [3,1,2],
                [3,2,1]
                ]
            self.assertEqual(set(tuple(x) for x in func([1,2,3])), set(tuple(x) for x in out))

if __name__ == '__main__':
    unittest.main()
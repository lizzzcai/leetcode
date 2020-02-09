'''
08/02/2020

710. Random Pick with Blacklist - Hard

Tag: Binary Search, Random, Sort, Hash Table

Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer from [0, N) which is NOT in B.

Optimize it such that it minimizes the call to system’s Math.random().

Note:

1 <= N <= 1000000000
0 <= B.length < min(100000, N)
[0, N) does NOT include N. See interval notation.
Example 1:

Input: 
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
Output: [null,0,0,0]
Example 2:

Input: 
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
Output: [null,1,1,1]
Example 3:

Input: 
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]
Example 4:

Input: 
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, N and the blacklist B. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.

'''

from typing import List
# Solution
from random import randrange
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        '''
        remap method
        https://leetcode.com/problems/random-pick-with-blacklist/discuss/146533/Super-Simple-Python-AC-w-Remapping
        Time: O(B)
        Space: O(B)
        '''
        b = set(blacklist)
        self.M = N - len(blacklist)
        need_remap = []
        for num in blacklist:
            if num < self.M:
                need_remap.append(num)
        self.hmap = {}
        j = 0
        for i in range(self.M, N):
            if i not in b:
                self.hmap[need_remap[j]] = i
                j += 1    

    def pick(self) -> int:
        idx = randrange(0, self.M)
        if idx in self.hmap:
            return self.hmap[idx]
        else:
            return idx
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        N = 4
        blacklist = [2]
        obj = Solution(N, blacklist)
        param_1 = obj.pick()
        self.assertIn(param_1, [0,1,3])

if __name__ == '__main__':
    unittest.main()
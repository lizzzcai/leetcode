'''
08/02/2020

528. Random Pick with Weight - Medium

Tag: Binary Search, Random

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.


'''

from typing import List
# Solution
from random import randrange
class Solution:

    def __init__(self, w: List[int]):
        self.n = len(w)
        self.arr = [0 for _ in range(self.n)]
        self.arr[0] = w[0]
        self.s = w[0]
        for i in range(1, self.n):
            self.arr[i] = self.arr[i-1] + w[i]
            self.s += w[i]    

    def pickIndex(self) -> int:
        '''
        https://leetcode.com/problems/random-pick-with-weight/discuss/154432/Very-easy-solution-based-on-uniform-sampling-with-explanation
        w = [2, 3, 4]
        arr = [2, 5, 9]
               0, 1, 2
        s = 9
        '''
        target = randrange(1, self.s+1)
        l, r = 0, self.n-1
        while l <= r:
            mid = (l+r) // 2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        w = [2,3,4]
        obj = Solution(w)
        param_1 = obj.pickIndex()
        self.assertIn(param_1, [0,1,2])

if __name__ == '__main__':
    unittest.main()
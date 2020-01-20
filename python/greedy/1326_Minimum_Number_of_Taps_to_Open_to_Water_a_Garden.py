'''
20/01/2020

1326. Minimum Number of Taps to Open to Water a Garden - Hard

Tag: Greedy, Dynamic Programming

There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

 

Example 1:


Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]
Example 2:

Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.
Example 3:

Input: n = 7, ranges = [1,2,1,0,2,1,0,1]
Output: 3
Example 4:

Input: n = 8, ranges = [4,0,0,0,0,0,0,0,4]
Output: 2
Example 5:

Input: n = 8, ranges = [4,0,0,0,4,0,0,0,4]
Output: 1
 

Constraints:

1 <= n <= 10^4
ranges.length == n + 1
0 <= ranges[i] <= 100

'''

from typing import List
# Solution
class Solution:
    '''
    https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/484341/Python-Jump-Game-II

    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_range = [0] * (n+1)
        
        for i, r in enumerate(ranges):
            left, right = max(0, i - r), min(n, i + r)
            max_range[left] = max(max_range[left], right - left)
        
        
        start, end, step = 0, 0, 0
        
        while end < n:
            step += 1
            start, end = end, max( i + max_range[i] for i in range(start, end + 1))
            if start == end:
                return -1
        
        return step
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().minTaps
        self.assertEqual(func(5, [3,4,1,1,0,0]), 1)
        self.assertEqual(func(3, [0,0,0,0]), -1)
        self.assertEqual(func(7, [1,2,1,0,2,1,0,1]), 3)
        self.assertEqual(func(8, [4,0,0,0,0,0,0,0,4]), 2)
        self.assertEqual(func(8, [4,0,0,0,4,0,0,0,4]), 1)



if __name__ == '__main__':
    unittest.main()
'''
30/04/2020

1. 945. Minimum Increment to Make Array Unique - Medium

Tag: Array

Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

 

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
 

Note:

0 <= A.length <= 40000
0 <= A[i] < 40000

'''

from typing import List
# Solution
class Solution1:
    '''
    TLE
    Time complexity : O(count)
    Space complexity : O(n)
    '''
    def minIncrementForUnique(self, A: List[int]) -> int:
        hmap = {}
        count = 0
        for x in A:
            if x in hmap:
                curr = x
                while curr in hmap:
                    curr += 1
                    count += 1
                hmap[curr] = 1

            else:
                hmap[x] = 1
        
        return count

import collections
class Solution2:
    '''
    Counting
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = collections.Counter(A)
        taken = []
        ans = 0
        for x in range(100000):
            if count[x] >= 2:
                taken.extend([x]*(count[x]-1))
            elif taken and count[x] == 0:
                ans += x - taken.pop()
        
        return ans


class Solution3:
    '''
    Counting
    Time complexity : O(nlogn)
    Space complexity : O(n)
    '''

    def minIncrementForUnique(self, A: List[int]) -> int:

        if not A:
            return 0
        
        A.sort()
        s, ans = A[0], 0
        for x in A:
            ans += max(0, s - x)
            s = max(s+1, x+1)
        
        return ans


class Solution4:
    '''
    Union Find, O(N)
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def minIncrementForUnique(self, A: List[int]) -> int:
        root = {}
        def find(x):
            root[x] = find(root[x] + 1) if x in root else x
            return root[x]
        return sum(find(a) - a for a in A)


class Solution5:
    def minIncrementForUnique(self, A: List[int]) -> int:
        level = -1 
        res = 0
        
        for x in sorted(A):
            if level < x:
                level = x
            else:
                level += 1
                res += level - x
        
        return res

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2(),Solution3(),Solution4(),Solution5()]:
            func = Sol.minIncrementForUnique
            self.assertEqual(func([1,2,2]), 1)
            self.assertEqual(func([3,2,1,2,1,7]), 6)
            self.assertEqual(func([3,2,1,2,1,1,1,7,1,1,3,4,20,10,10,2,3,2,1,1,7]), 148)

if __name__ == '__main__':
    unittest.main()
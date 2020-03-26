'''
26/03/2020

216. Combination Sum III - Medium

Tag: Backtracking

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''

from typing import List
class Solution1:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        '''
        Time: O(9^K)
        '''
        def backtrack(start, kleft, nleft, track):
            if kleft == 0 and nleft == 0:
                res.append(track[:])
            
            for i in range(start, 10):
                if i > nleft:
                    break
                track.append(i)
                backtrack(i+1, kleft-1, nleft-i, track)
                track.pop()
        
        res = []
        backtrack(1, k, n, [])
        
        return res

class Solution2:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(start, kleft, nleft, track):
            if kleft == 0 and nleft == 0:
                res.append(track[:])
            
            # 10-kleft+1 to stop early if no enough select left to choose
            for i in range(start, 10-kleft+1):
                # break if n-i < 0
                if i > nleft:
                    break
                track.append(i)
                backtrack(i+1, kleft-1, nleft-i, track)
                track.pop()
        
        
        res = []
        backtrack(1, k, n, [])
        
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
            func = Sol.combinationSum3
            self.assertEqual(set(tuple(x) for x in func(3,7)), set(tuple(x) for x in [[1,2,4]]))
            self.assertEqual(set(tuple(x) for x in func(3,9)), set(tuple(x) for x in [[1,2,6], [1,3,5],[2,3,4]]))
            self.assertEqual(set(tuple(x) for x in func(3,15)), set(tuple(x) for x in [[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]]))


if __name__ == '__main__':
    unittest.main()
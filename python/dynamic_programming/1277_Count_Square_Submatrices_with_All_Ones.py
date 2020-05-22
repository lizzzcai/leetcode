'''
01/05/2020

1277. Count Square Submatrices with All Ones - Medium

Tag: Array, Dynamic Programming

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n^3)
    Space complexity : O(1)
    '''
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 1:
                    for d in range(min(len(matrix)-r, len(matrix[0])-c)):
                        if sum(sum(matrix[i][j] for i in range(r, r+d+1)) for j in range(c, c+d+1)) == (d+1)**2:
                            res += 1
                        else:
                            break
        
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
            func = Sol.countSquares
            self.assertEqual(func([[0,1,1,1],[1,1,1,1],[0,1,1,1]]), 15)
            self.assertEqual(func([[1,0,1],[1,1,0], [1,1,0]]), 7)


if __name__ == '__main__':
    unittest.main()
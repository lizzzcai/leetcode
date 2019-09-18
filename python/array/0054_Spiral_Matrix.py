"""
18/09/2019
54. Spiral Matrix - Medium
Tag: Array

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Time: O(n*m)
        Space: O(n*m)
        """
        if not matrix:
            return []

        d = [(1,0), (0,1), (-1,0), (0,-1)]
        m, n = len(matrix[0]), len(matrix)
        record = [[False for _ in range(m)] for _ in range(n)]
        print(f"m: {m}, n: {n}")
        

        idx = 0
        x, y = 0, 0
        res = []
        #record[0][0] = True
        for _ in range(m*n):
            print(f"x: {x}, y: {y}")
            record[y][x] = True
            res.append(matrix[y][x])
            print(f"value: {matrix[y][x]}")

            next_x, next_y = x + d[idx%4][0], y + d[idx%4][1]
            print(f"next_x: {next_x}, next_y: {next_y}")
            if (next_x < 0 or next_x > m-1) or (next_y < 0 or next_y > n-1) or record[next_y][next_x]:
                idx += 1
                print(f"idx: {idx}")
            #if (0<= next_x <= m-1) and (0 <= next_y <= n-1) and not record[next_y][next_x]:
            x, y = x + d[idx%4][0], y + d[idx%4][1]
        
        return res
        
        

# Unit Test
import unittest
class spiralOrderCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_spiralOrder(self):
        func = Solution().spiralOrder
 

        self.assertEqual(func([
                            [ 1, 2, 3 ],
                            [ 4, 5, 6 ],
                            [ 7, 8, 9 ]
                            ]), [1,2,3,6,9,8,7,4,5])

        self.assertEqual(func([
                            [1, 2, 3, 4],
                            [5, 6, 7, 8],
                            [9,10,11,12]
                            ]), [1,2,3,4,8,12,11,10,9,5,6,7])


        self.assertEqual(func([
                            ]), [])







if __name__ == '__main__':
    unittest.main()



'''
21/02/2020

1042. Flower Planting With No Adjacent - Easy

Tag: Graph, Greedy

You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

 

Example 1:

Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Example 2:

Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
 

Note:

1 <= N <= 10000
0 <= paths.size <= 20000
No garden has 4 or more paths coming into or leaving it.
It is guaranteed an answer exists.
'''

from typing import List
import collections
# Solution
class Solution1:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        
        garden_paths = collections.defaultdict(list)
        for x, y in paths:
            garden_paths[x].append(y)
            garden_paths[y].append(x)
        
        res = {}
        for i in range(1, N+1):
            exist_flowers = set([res[garden] for garden in garden_paths[i] if garden in res])
            for j in range(1, 5):
                if j not in exist_flowers:
                    res[i] = j
        
        return [res[i] for i in range(1, N+1)]

class Solution2:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        
        '''
        Time: O(N)
        Space: O(N)
        
        '''
        res = [0] * N
        count = [[] for _ in range(N)]
        for x, y in paths:
            count[x-1].append(y-1)
            count[y-1].append(x-1)
        for i in range(N):
            res[i] = ({1,2,3,4} - {res[j] for j in count[i]}).pop()
        
        return res
            
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):

        for func in [Solution1().gardenNoAdj, Solution2.gardenNoAdj]:
            self.assertEqual(func(3, [[1,2],[2,3],[3,1]]), [1,2,3])
            self.assertEqual(func(4, [[1,2],[3,4]]), [1,2,1,2])
            self.assertEqual(func(4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]), [1,2,3,4])


if __name__ == '__main__':
    unittest.main()
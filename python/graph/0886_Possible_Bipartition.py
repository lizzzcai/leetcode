'''
28/05/2020

886. Possible Bipartition - Medium

Tag: DFS

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
 

Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].

'''

from typing import List
import collections
# Solution
class Solution1:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        '''
        Depth-First Search
        Time: O(N+E) E is the length of dislikes
        Space (N+E)
        '''
        graph= collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        color = {}
        def dfs(node, c = 0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c^1) for nei in graph[node])
        
        return all(dfs(node) for node in range(1, N+1) if node not in color)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.possibleBipartition
            self.assertEqual(func(4, [[1,2],[1,3],[2,4]]), True)
            self.assertEqual(func(3, [[1,2],[1,3],[2,3]]), False)
            self.assertEqual(func(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]), False)




if __name__ == '__main__':
    unittest.main()
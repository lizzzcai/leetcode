'''
01/06/2020

787. Cheapest Flights Within K Stops - Medium

Tag: Dynamic Programming, Heap, Breadth-first Search

There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
 

Constraints:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.

'''

from typing import List
# Solution
import collections, math
class Solution1:
    '''
    Time complexity : O(m*k)
    Space complexity : O(n)
    '''
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        '''
        https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/115541/JavaPython-Priority-Queue-Solution
        https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/317262/2-Clean-Python-Solution-(BFS-Dijkstra-Explained)
        BFS
        '''
        if n == 1:
            return 0
        
        f = collections.defaultdict(dict)
        for s, d, p in flights:
            f[s][d] = p
        
        q = collections.deque([(0, src, K+1)])
        res = math.inf
        while q:
            cost, curr, k = q.popleft()
            if curr == dst:
                res = min(res, cost)
            
            if k > 0:
                for d, p in f[curr].items():
                    if cost+p < res:
                        q.append((cost+p, d, k-1))
    
        if res != math.inf:
            return res
        return -1

import heapq
class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        '''
        https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/115541/JavaPython-Priority-Queue-Solution
        piority queue
        '''
        if n == 1:
            return 0
        
        f = collections.defaultdict(dict)
        for s, d, p in flights:
            f[s][d] = p
        
        q = []
        heapq.heappush(q, (0, src, K+1))
        
        while q:
            cost, curr, k = heapq.heappop(q)
            if curr == dst:
                return cost
            
            if k > 0:
                for d, p in f[curr].items():
                    heapq.heappush(q, (cost+p, d, k-1))
        
        return -1

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.findCheapestPrice
            self.assertEqual(func(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1), 200)
            self.assertEqual(func(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0), 500)


if __name__ == '__main__':
    unittest.main()
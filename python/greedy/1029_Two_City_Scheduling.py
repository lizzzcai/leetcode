'''
03/06/2020

1029. Two City Scheduling - Easy

Tag: Greedy

There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000

'''

from typing import List
# Solution
class Solution1:
    '''
    Time O(nlogn)
    Space O(n)
    '''
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key=lambda x: x[0]-x[1])
        return sum(x[0] if idx < len(costs)//2 else x[1] for idx, x in enumerate(costs))

class Solution2:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        self.sort(costs, 0, n-1, n//2)
        return sum(x[0] if idx < n//2 else x[1] for idx, x in enumerate(costs))
    
    def sort(self, costs, l, r, K):
        if l < r:
            p = self.partition(costs, l, r)
            if p == K:
                return
            elif p < K:
                self.sort(costs, p+1, r, K)
            else:
                self.sort(costs, l, p-1, K)
    
    def partition(self, costs, l, r):
        pivot = costs[r][0] - costs[r][1]
        a = l
        for i in range(l, r):
            if costs[i][0] - costs[i][1] <= pivot:
                # swap i and a
                costs[i], costs[a] = costs[a], costs[i]
                a += 1
        # swap the pivot and a
        costs[r], costs[a] = costs[a], costs[r]
        return a  

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.twoCitySchedCost
            self.assertEqual(func([[10,20],[30,200],[400,50],[30,20]]), 110)
            self.assertEqual(func([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]), 1859)
if __name__ == '__main__':
    unittest.main()
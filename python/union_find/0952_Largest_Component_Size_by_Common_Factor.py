'''
12/06/2020

952. Largest Component Size by Common Factor - Hard

Tag: Math, Union Find

Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

 

Example 1:

Input: [4,6,15,35]
Output: 4

Example 2:

Input: [20,50,9,63]
Output: 2

Example 3:

Input: [2,3,6,7,4,12,21,39]
Output: 8

Note:

1 <= A.length <= 20000
1 <= A[i] <= 100000

'''

from typing import List
import collections

# Solution
class DSU:
    def __init__(self, N):
        self.p = [x for x in range(N)]
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution1:
    def largestComponentSize(self, A: List[int]) -> int:
        B = []
        for x in A:
            facs = []
            d = 2
            while d*d <= x:
                if x % d == 0:
                    while x % d == 0:
                        x /= d
                    facs.append(d)
                d += 1
            
            if x > 1 or not facs:
                facs.append(x)
            B.append(facs)
        
        primes = list({p for facs in B for p in facs})
        prime_to_index = {p:i for i, p in enumerate(primes)}
        
        dsu = DSU(len(primes))
        for facs in B:
            for x in facs:
                dsu.union(prime_to_index[facs[0]], prime_to_index[x])
        
        count = collections.Counter(dsu.find(prime_to_index[facs[0]]) for facs in B)
        
        return max(count.values())

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.largestComponentSize
            self.assertEqual(func([4,6,15,35]), 4)
            self.assertEqual(func([20,50,9,63]), 2)
            self.assertEqual(func([2,3,6,7,4,12,21,39]), 8)


if __name__ == '__main__':
    unittest.main()
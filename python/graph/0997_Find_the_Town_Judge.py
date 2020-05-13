'''
20/02/2020
11/05/2020

997. Find the Town Judge - Easy

Tag: Graph

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 

Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N

'''

from typing import List
import collections
# Solution
class Solution1:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        trust_collect = collections.defaultdict(set)
        for a, b in trust:
            # a trusts a person b
            trust_collect[a].add(b)
        
        if len(trust_collect) != N-1:
            return -1
        
        for i in range(1,N+1):
            if i not in trust_collect:
                for value in trust_collect.values():
                    if i not in value:
                        return -1
                return i
        
        return -1

class Solution2:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0] * (N+1)
        for a, b in trust:
            count[a] -= 1
            count[b] += 1
        
        for i in range(1, N+1):
            if count[i] == N-1:
                return i
        
        return -1


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for func in [Solution1().findJudge, Solution2().findJudge]:
            self.assertEqual(func(1, []), 1)
            self.assertEqual(func(10, []), -1)

            self.assertEqual(func(2, [[1,2]]), 2)
            self.assertEqual(func(3, [[1,3],[2,3]]), 3)
            self.assertEqual(func(3, [[1,3],[2,3],[3,1]]), -1)
            self.assertEqual(func(3, [[1,2],[2,3]]), -1)
            self.assertEqual(func(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]), 3)





if __name__ == '__main__':
    unittest.main()
'''
28/06/2020

332. Reconstruct Itinerary - Medium

Tag: Graph, DFS

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.

'''

from typing import List
import collections
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        https://leetcode.com/problems/reconstruct-itinerary/discuss/78799/Very-Straightforward-DFS-Solution-with-Detailed-Explanations
        
        '''
        N = len(tickets) + 1
        
        # create a graph
        hmap = collections.defaultdict(list)
        for fm, to in tickets:
            hmap[fm].append(to)
        # sort the destination in lexical order
        for key in hmap:
            if len(hmap[key]) > 1:
                hmap[key].sort()
        
        
        
        def dfs(airport, i, N, itinerary):
            nonlocal res

            if i == N:
                res = itinerary[:]
                return
            
            for idx, x in enumerate(hmap[airport]):
                if x == "###":
                    continue

                if res:
                    break
                
                hmap[airport][idx] = "###"
                dfs(x, i+1, N, itinerary+[x])
                hmap[airport][idx] = x
        
        
        
        res = []
        dfs("JFK", 1, N, ["JFK"])
        
        return res
        

class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        Time: O(E+V)
        Space: O(E+V)
        https://leetcode.com/problems/reconstruct-itinerary/discuss/375397/Simply-simple-Python-Solution-Using-stack-for-dfs-with-comments
        
        '''
        N = len(tickets) + 1
        
        # create a graph
        hmap = collections.defaultdict(list)
        for fm, to in tickets:
            hmap[fm].append(to)
        # sort the destination in lexical order
        for key in hmap:
            if len(hmap[key]) > 1:
                hmap[key].sort(reverse=True)
                
        res = []
        stack = ["JFK"]
        while stack:
            curr = stack[-1]
            if len(hmap[curr]) > 0:
                stack.append(hmap[curr].pop())
            else:
                res.append(stack.pop())

        
        return res[::-1]
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.findItinerary
            self.assertEqual(func([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]), ["JFK", "MUC", "LHR", "SFO", "SJC"])
            self.assertEqual(func([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]), ["JFK","ATL","JFK","SFO","ATL","SFO"])


if __name__ == '__main__':
    unittest.main()
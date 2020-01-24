'''
22/01/2020

399. Evaluate Division - Medium

Tag: Graph, DFS

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.


'''

from typing import List
from collections import deque, defaultdict

# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = self.build_graph(equations, values)
        res = []
        for query in queries:
            visited = set()
            val = self.dfs(graph, visited, query[0], query[1], 1.0)
            res.append(val)
        return res
    
    def build_graph(self, equations, values):
        graph = defaultdict(dict)

        def add_edge(numerator, denominator, value):
            graph[numerator][denominator] = value
        
        for ([numerator, denominator], value) in zip(equations, values):
            add_edge(numerator, denominator, value)
            add_edge(denominator, numerator, 1./value)
        
        return graph

    def dfs(self, graph, visited, src, dst, value):
        if src not in graph or dst not in graph:
            return -1.0
        
        if src == dst:
            return value
    
        visited.add(src)
        src_node = graph.get(src)
        for connection in src_node:
            if connection not in visited:
                val = self.dfs(graph, visited, connection, dst, src_node[connection] * value)
                if val != -1.0:
                    return val

        return -1.0

class Solution2:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.build_graph(equations, values)
        res = []
        for query in queries:
            val = self.bfs(graph, query[0], query[1])
            res.append(val)
            if val != -1.0:
                # add cache
                graph[query[0]][query[1]] = val
                graph[query[1]][query[0]] = 1./val
        return res
    
    def build_graph(self, equations, values):
        graph = defaultdict(dict)

        def add_edge(numerator, denominator, value):
            graph[numerator][denominator] = value
        
        for ([numerator, denominator], value) in zip(equations, values):
            add_edge(numerator, denominator, value)
            add_edge(denominator, numerator, 1./value)
        
        return graph
    
    def bfs(self, graph, src, dst):
        if src not in graph or dst not in graph:
            return -1.0

        q = deque([(src, 1.0)])
        visited = set()

        while q:
            node, curr_product = q.popleft()
            if node == dst:
                return curr_product
            for neighbor, val in graph[node].items():
                if neighbor not in visited:
                    q.append((neighbor, curr_product * val))
                    visited.add(neighbor)
        
        return -1.0

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
            pass

    def test_testCase(self):
        func = Solution1().calcEquation
        self.assertEqual(func([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]), [6.00000,0.50000,-1.00000,1.00000,-1.00000])
       
        func = Solution2().calcEquation
        self.assertEqual(func([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]), [6.00000,0.50000,-1.00000,1.00000,-1.00000])

if __name__ == '__main__':
    unittest.main()
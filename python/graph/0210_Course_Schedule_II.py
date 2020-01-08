'''
30/12/2019

210. Course Schedule II - Medium

Tag: Graph, BFS, DFS


There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

'''

from typing import List
# Solution 1 - BFS
class Solution1:
    '''
    The time efficiency is O(V^2+VE), because each dfs in adjacency list is O(V+E) and we do it V times .
    for i in xrange(numCourses): O(V) . * dfs() O(V+E)
    Space efficiency is O(E).
    '''
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        courses_set = set()
        num_of_prerequisites = dict()
        prerequisite_for = dict()
        # init the dict and set
        for i in range(numCourses):
            courses_set.add(i)
            num_of_prerequisites[i] = 0
            prerequisite_for[i] = []
        
        # order to store result
        orders = []
        # iterate the prerequisites
        for pair in prerequisites:
            key, value = pair[0], pair[1]

            # add one on the number of prerequisiste needed for the given courses
            num_of_prerequisites[key] = num_of_prerequisites[key] + 1

            # add course into list of courses need this course as prerequisiste
            prerequisite_for[value] = prerequisite_for[value] + [key]

        courses_without_prerequistite = [c for c in courses_set if num_of_prerequisites[c] == 0]
        
        while courses_without_prerequistite:
            course = courses_without_prerequistite.pop(0)
            # get the list of courses need this course as prerequisite
            courses_rely_on_this = prerequisite_for[course]
            for c in courses_rely_on_this:
                num_of_prerequisites[c] -= 1
                if num_of_prerequisites[c] == 0:
                    courses_without_prerequistite.append(c)
            
            # add the course into order
            orders.append(course)
            
        for c in courses_set:
            if num_of_prerequisites[c] != 0:
                return []
        return orders

# Solution 2 - DFS
from collections import defaultdict
class Solution2:
    '''
    The time efficiency is O(V^2+VE), because each dfs in adjacency list is O(V+E) and we do it V times .
    for i in xrange(numCourses): O(V) . * dfs() O(V+E)
    Space efficiency is O(E).
    '''
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # init graph and visited
        graph = defaultdict(list)
        visited = [0 for _ in range(numCourses)]
        # create the graph
        for pair in prerequisites:
            course, prerequisite = pair
            graph[course].append(prerequisite)
        
        # init the orders
        orders = []
        # start to visit each node
        for course in range(numCourses):
            if not self.dfs(graph, visited, orders, course):
                return []
        return orders
    
    def dfs(self, graph, visited, orders, i):
        '''
        if node v has not been visited, then mark it as 0.
        if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
        if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.
        
        '''
        # if the node was marked as being visited, then a cycle is found
        if visited[i] == -1:
            return False
        # if it is done visted, then do not visit again
        if visited[i] == 1:
            return True
        # mark the node as being visited
        visited[i] = -1
        # visit all the neighours
        for j in graph[i]:
            if not self.dfs(graph, visited, orders, j):
                return False
        
        # add into orders
        orders.append(i)
        # after visit all the neighbours, mark it as done visited
        visited[i] = 1
        
        return True
            

# Unit Test
import unittest
class findOrderCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_findOrderCase(self):
        func = Solution1().findOrder
        self.assertEqual(func(2, [[1,0]]), [0,1])
        self.assertEqual(func(4, [[1,0],[2,0],[3,1],[3,2]]), [0,1,2,3])
        self.assertEqual(func(1, []), [0])
        func = Solution2().findOrder
        self.assertEqual(func(2, [[1,0]]), [0,1])
        self.assertEqual(func(4, [[1,0],[2,0],[3,1],[3,2]]), [0,1,2,3])
        self.assertEqual(func(1, []), [0])


if __name__ == '__main__':
    unittest.main()
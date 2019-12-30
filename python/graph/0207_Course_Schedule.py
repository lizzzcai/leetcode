'''
30/12/2019

207. Course Schedule - Medium

Tag: Graph, BFS, DFS


There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

'''

from typing import List
# Solution 1 - BFS
class Solution:
    '''
    BFS
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # init storage to store the courses, the number of prerequisite for each course and the course list taking this course as prerequistie.
        courses_set = set()
        num_of_prerequisites = dict()
        prerequisite_for = dict()
        
        # iterate hte prerequisites
        for pair in prerequisites:
            key, value = pair[0], pair[1]
            # add into courses set
            if key not in courses_set:
                courses_set.add(key)
            if value not in courses_set:
                courses_set.add(value)
            # add one on the number of prerequisiste needed for the given courses
            num_of_prerequisites[key] = num_of_prerequisites.setdefault(key, 0) + 1
            num_of_prerequisites[value] = num_of_prerequisites.setdefault(value, 0)

            # add course into list of courses need this course as prerequisiste
            prerequisite_for[value] = prerequisite_for.setdefault(value, []) + [key]

        courses_without_prerequistite = [c for c in courses_set if num_of_prerequisites[c] == 0]
        
        while courses_without_prerequistite:
            course = courses_without_prerequistite.pop(0)
            # get the list of courses need this course as prerequisite
            courses_rely_on_this = prerequisite_for.setdefault(course, [])
            for c in courses_rely_on_this:
                num_of_prerequisites[c] -= 1
                if num_of_prerequisites[c] == 0:
                    courses_without_prerequistite.append(c)
        
        for c in courses_set:
            if num_of_prerequisites[c] != 0:
                return False
        return True

# Unit Test
import unittest
class canFinishCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_canFinishCase(self):
        func = Solution().canFinish
        self.assertEqual(func(2, [[1,0]]), True)
        self.assertEqual(func(2, [[1,0], [0,1]]), False)


if __name__ == '__main__':
    unittest.main()
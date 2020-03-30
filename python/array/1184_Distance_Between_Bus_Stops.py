'''
30/03/2020

1184. Distance Between Bus Stops - Easy

Tag: Array

A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.

 

Example 1:



Input: distance = [1,2,3,4], start = 0, destination = 1
Output: 1
Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.
 

Example 2:



Input: distance = [1,2,3,4], start = 0, destination = 2
Output: 3
Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.
 

Example 3:



Input: distance = [1,2,3,4], start = 0, destination = 3
Output: 4
Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.
 

Constraints:

1 <= n <= 10^4
distance.length == n
0 <= start, destination < n
0 <= distance[i] <= 10^4

'''

from typing import List
# Solution
class Solution1:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        '''
        Time: O(n)
        Space: O(1)
        
        '''
        # base case
        if start == destination:
            return 0
        
        total, dist = 0, 0
        flag = False
        
        for i, val in enumerate(distance):
            total += val
            if i == start or i == destination:
                flag = not flag
            if flag:
                dist += val
        
        return min(dist, total-dist)
                

class Solution2:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        '''
        Time: O(n)
        Space: O(1)
        
        '''
        # base case
        if start == destination:
            return 0
        
        if start > destination:
            start, destination = destination, start
        
        return min(sum(distance[start:destination]), sum(distance[:start])+ sum(distance[destination:]))

            


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.distanceBetweenBusStops
            self.assertEqual(func([1,2,3,4], 0,1), 1)
            self.assertEqual(func([1,2,3,4], 0,2), 3)
            self.assertEqual(func([1,2,3,4], 0,3), 4)
            self.assertEqual(func([1,2,3,4], 3,1), 5)




if __name__ == '__main__':
    unittest.main()
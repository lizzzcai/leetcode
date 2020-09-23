'''
22/09/2020

1094. Car Pooling - Medium

Tag: Greedy

You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
 
 

Constraints:

trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamps = [0] * 1001
        for t in trips:
            timestamps[t[1]] += t[0]
            timestamps[t[2]] -= t[0]
        
        passengers = 0
        for ts in timestamps:
            passengers += ts
            if passengers > capacity:
                return False
            
        return True
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.carPooling
            self.assertEqual(func([[9,3,6],[8,1,7],[6,6,8],[8,4,9],[4,2,9]], 28), False)
            self.assertEqual(func([[5,1,3],[5,3,6],[1,1,2],[9,2,5],[6,5,7],[2,3,6],[9,3,5]], 26), True)


if __name__ == '__main__':
    unittest.main()
'''
30/05/2020

973. K Closest Points to Origin - Medium

Tag: Divide and Conquer, Heap, Sort

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000

'''

from typing import List
import heapq
# Solution
class Solution1:
    '''
    heap

    Time complexity : O(NlogK)
    Space complexity : O(K)
    '''
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for i in range(K):
            heapq.heappush(heap, (-(points[i][0]**2 + points[i][1]**2), i))
        
        for i in range(K, len(points)):
            dist = -(points[i][0]**2 + points[i][1]**2)
            if dist > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (dist, i))
        
        res = []
        for _ in range(K):
            res.append(points[heapq.heappop(heap)[1]])
            
        return res

class Solution2:
    '''
    heap

    Time complexity : O(NlogK)
    Space complexity : O(K)
    '''
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(heap, (-dist, point))
            if len(heap) > K:
                heapq.heappop(heap)
        
        return [tuple[1] for tuple in heap]



class Solution3:
    '''
    Sort

    Time complexity : O(NlogN)
    Space complexity : O(N)
    '''
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        points.sort(key=lambda x: x[0]**2+x[1]**2)
        
        return points[:K]


class Solution4:
    '''
    Divide and conquer
    Time: O(n)
    Space: O(n)

    
    '''

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        self.sort(points,0, len(points)-1, K)
        return points[:K]
    
    def sort(self, points, l, r, K):
        if l < r:
            p = self.partition(points, l, r)
            if p == K:
                return
            elif p < K:
                self.sort(points, p+1, r, K)
            else:
                self.sort(points, l, p-1, K)
    
    def partition(self, points, l, r):
        # select last point as pivot
        pivot = points[r]
        a = l
        for i in range(l, r):
            # compare the distance with pivot
            if (points[i][0]**2 + points[i][1]**2) <= (pivot[0]**2 + pivot[1]**2):
                # swap i and a
                points[i], points[a] = points[a], points[i]
                a += 1
        
        # swap the pivot with a
        points[a], points[r] = points[r], points[a]
        # return the index of pivot
        return a
                

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(), Solution3(),Solution4()]:
            func = Sol.kClosest
            self.assertCountEqual(func([[1,3],[-2,2]], 1), [[-2,2]])
            self.assertCountEqual(func([[3,3],[5,-1],[-2,4]], 2), [[3,3],[-2,4]])


if __name__ == '__main__':
    unittest.main()
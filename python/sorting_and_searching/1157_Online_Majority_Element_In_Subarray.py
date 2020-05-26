'''
24/05/2020

1157. Online Majority Element In Subarray - Hard

Tag: Array, Binary Search, Segment Tree

Implementing the class MajorityChecker, which has the following API:

MajorityChecker(int[] arr) constructs an instance of MajorityChecker with the given array arr;
int query(int left, int right, int threshold) has arguments such that:
0 <= left <= right < arr.length representing a subarray of arr;
2 * threshold > right - left + 1, ie. the threshold is always a strict majority of the length of the subarray
Each query(...) returns the element in arr[left], arr[left+1], ..., arr[right] that occurs at least threshold times, or -1 if no such element exists.

 

Example:

MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
majorityChecker.query(0,5,4); // returns 1
majorityChecker.query(0,3,3); // returns -1
majorityChecker.query(2,3,2); // returns 2
 

Constraints:

1 <= arr.length <= 20000
1 <= arr[i] <= 20000
For each query, 0 <= left <= right < len(arr)
For each query, 2 * threshold > right - left + 1
The number of queries is at most 10000

'''

from typing import List
# Solution
import collections
from random import randrange
class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.A = arr
        self.a2i = collections.defaultdict(list)
        for idx, x in enumerate(arr):
            self.a2i[x].append(idx)
        

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            a = self.A[randrange(left, right+1)]
            arr = self.a2i[a]
            l = self.find_left(arr, left)
            r = self.find_right(arr, right)
            if r-l+1 >= threshold:
                return a
            
        return -1
    
    def find_left(self, arr, target):
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l+r)//2
            if arr[mid] >= target:
                r = mid-1
            else:
                l = mid + 1
        
        return l
    
    def find_right(self, arr, target):
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l+r)//2
            if arr[mid] > target:
                r = mid-1
            else:
                l = mid + 1
        
        return r



# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [MajorityChecker]:
            func = Sol([1,1,2,2,1,1])
            self.assertEqual(func.query(0,5,4), 1)
            self.assertEqual(func.query(0,3,3), -1)
            self.assertEqual(func.query(2,3,2), 2)

            func = Sol([1,2,1,2,2,2,1,2,2,2,1,1,2,2,2,2,1,1,2,1,1,2,2,2,1])
            self.assertEqual(func.query(10,16,7), -1)
            self.assertEqual(func.query(22,24,2),2)
            self.assertEqual(func.query(2,9,6), 2)
            self.assertEqual(func.query(7,24,17), -1)
            self.assertEqual(func.query(7,20,13), -1)
            self.assertEqual(func.query(3,18,14), -1)
            self.assertEqual(func.query(9,16,6), -1)
            self.assertEqual(func.query(3,6,4), -1)
            self.assertEqual(func.query(6,14,6), 2)
            self.assertEqual(func.query(2,4,3), -1)








if __name__ == '__main__':
    unittest.main()
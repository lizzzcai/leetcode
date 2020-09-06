'''
05/09/2020

295. Find Median from Data Stream - Hard

Tag: Design, Heap

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

'''

from typing import List
import bisect
# Solution

class MedianFinder1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.size = 0
        
    def find_right(self, arr, target):
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l+r)//2
            if arr[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return l
        
    def addNum(self, num: int) -> None:
        idx = self.find_right(self.data, num)
        self.data = self.data[:idx]+[num]+self.data[idx:]
        self.size += 1
        
    def findMedian(self) -> float:
        return self.data[self.size//2] if self.size%2==1 else 0.5*(self.data[self.size//2] + self.data[self.size//2-1])
import heapq
        

class MedianFinder2:

    def __init__(self):
        """
        https://leetcode.com/problems/find-median-from-data-stream/solution/
        initialize your data structure here.
        """
        self.lh = [] # max heap
        self.rh = [] # min heap
        
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.lh, -num)
        heapq.heappush(self.rh, -self.lh[0])
        heapq.heappop(self.lh)
        if len(self.lh) < len(self.rh):
            heapq.heappush(self.lh, -self.rh[0])
            heapq.heappop(self.rh)
        
        
    def findMedian(self) -> float:
        return -self.lh[0] if len(self.lh) > len(self.rh) else 0.5*(self.rh[0] - self.lh[0])
        


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [MedianFinder1(), MedianFinder2()]:
            func = Sol
            func.addNum(1)
            func.addNum(2)
            self.assertEqual(func.findMedian(), 1.5)
            func.addNum(3)
            self.assertEqual(func.findMedian(), 2)


if __name__ == '__main__':
    unittest.main()
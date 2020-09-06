'''
05/09/2020

480. Sliding Window Median - Hard

Tag: Sliding Windows

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
Answers within 10^-5 of the actual value will be accepted as correct.

'''

from typing import List
import bisect
# Solution
class Solution1:
    '''
    Time complexity : O(nlogk)
    Space complexity : O(k)
    '''
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        '''
        https://leetcode.com/problems/sliding-window-median/discuss/96337/Python-SortedArray-(beats-100)-and-2-Heap(beats-90)-solution
        '''
        win = nums[:k]
        res = []
        
        win.sort()
        is_odd = k % 2
        
        for i in range(k, len(nums)):
            median = (win[k//2] + win[k//2-1])*0.5 if not is_odd else win[k//2]
            res.append(median)
            # pop the last one out
            win.pop(bisect.bisect_right(win, nums[i-k])-1) # find index of first element larger than target
            bisect.insort(win, nums[i]) # O(n)
        median = (win[k//2] + win[k//2-1])*0.5 if not is_odd else win[k//2]
        res.append(median)
        
        return res

import heapq
class Solution2:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        '''
        https://leetcode.com/problems/sliding-window-median/discuss/96337/Python-SortedArray-(beats-100)-and-2-Heap(beats-90)-solution
        O(N logK)
        '''
        lh, rh = [], [] # lh: max heap, rh: min heap, (value, index)
        res = []
        is_odd = k % 2
        
        # assign the first k items into lh
        # after that pop the top k-k/2 items into rh
        # so lh has k/2 items and rh has k-k/2 items
        for i, n in enumerate(nums[:k]):
            heapq.heappush(lh, (-n, i))
        for _ in range(k-k//2):
            heapq.heappush(rh, (-lh[0][0], lh[0][1]))
            heapq.heappop(lh)
        
        for i in range(k, len(nums)):
            # calculate the mean
            res.append(rh[0][0] if is_odd else (rh[0][0]-lh[0][0])/2)
            curr = nums[i]
            if curr >= rh[0][0]:
                # append it into right heap
                heapq.heappush(rh, (curr, i))
                # check if the left item at i-k at lh
                # if yes, move one element from rh to lh to make it balanced
                if nums[i-k] <= rh[0][0]: # heap first sort by order, second sort by index
                    heapq.heappush(lh, (-rh[0][0], rh[0][1]))
                    heapq.heappop(rh)
                # else: pass
            else:
                # append curr into left heap
                heapq.heappush(lh, (-curr, i))
                # check if the left item at i-k at rh
                # if yes, move one element from lh to rh to make it alanced
                if nums[i-k] >= rh[0][0]:
                    heapq.heappush(rh, (-lh[0][0], lh[0][1]))
                    heapq.heappop(lh)
                # else: pass
            
            # lazy delete the item out of bound
            while lh and lh[0][1] <= i-k:
                heapq.heappop(lh)
            while rh and rh[0][1] <= i-k:
                heapq.heappop(rh)
        
        res.append(rh[0][0] if is_odd else (rh[0][0]-lh[0][0])/2)
        
        return res
        


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.medianSlidingWindow
            self.assertEqual(func([1,3,-1,-3,5,3,6,7], 3), [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000])
            self.assertEqual(func([1,2,3,4,2,3,1,4,2], 3), [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000])



if __name__ == '__main__':
    unittest.main()
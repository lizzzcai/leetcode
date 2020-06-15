'''
14/06/2020

668. Kth Smallest Number in Multiplication Table - Hard

Tag: Binary Search

Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?

Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.

Example 1:
Input: m = 3, n = 3, k = 5
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).
Example 2:
Input: m = 2, n = 3, k = 6
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
Note:
The m and n will be in the range [1, 30000].
The k will be in the range [1, m * n]

'''

from typing import List
# Solution
import heapq
class Solution1:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        '''
        TLE
        using heap
        '''
        heap = []
        def push(i, j):
            if i <= m and j <= n:
                heapq.heappush(heap, (i*j, i, j))
        
        push(1, 1)
        res = 1
        while heap and k > 0:
            val, i, j = heapq.heappop(heap)
            res = val
            push(i, j+1)
            if j == 1:
                push(i+1, 1)
            k -= 1
        
        return res


class Solution2:
    '''
    Time complexity : O(mlog(n*m))
    Space complexity : O(1)
    '''
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        l, h = 1, m*n
        
        while l <= h:
            mid = (l+h) // 2
            count = 0
            j = n
            for i in range(1, m+1):
                while j > 0 and i*j > mid:
                    j-=1
                if j > 0:
                    count += j
            
            if count < k:
                l = mid + 1
            else:
                h = mid - 1
            
        return l


class Solution3:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        def enough(x):
            count = 0
            for i in range(1, m+1):
                count += min(x//i, n)
            return count >= k
        
        l, h = 1, m*n
        
        while l <= h:
            mid = (l+h) // 2

            if not enough(mid):
                l = mid + 1
            else:
                h = mid - 1
            
        return l


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(), Solution3()]:
            func = Sol.findKthNumber
            self.assertEqual(func(3,3,5), 3)
            self.assertEqual(func(2,3,6), 6)
            self.assertEqual(func(38,40,955), 437)



if __name__ == '__main__':
    unittest.main()
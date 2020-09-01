'''
01/09/2020

949. Largest Time for Given Digits - Easy

Tag: Math

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""
 

Note:

A.length == 4
0 <= A[i] <= 9

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(1)
    Space complexity : O(1)
    '''
    def largestTimeFromDigits(self, A: List[int]) -> str:
        max_time = -1
        
        def build_time(arr):
            nonlocal max_time
            h,i,j,k = arr
            hours = h*10+i
            minues = j*10+k
            if hours < 24 and minues < 60:
                max_time = max(max_time, hours*60+minues)
                
        def permutate(arr, start):
            if start == len(arr):
                build_time(arr)
                return
            
            for i in range(start, len(arr)):
                arr[i], arr[start] = arr[start], arr[i]
                permutate(arr, start+1)
                arr[i], arr[start] = arr[start], arr[i]
        
        
        permutate(A, 0)
        if max_time == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.largestTimeFromDigits
            self.assertEqual(func([1,2,3,4]), "23:41")
            self.assertEqual(func([5,5,5,5]), "")
            self.assertEqual(func([0,0,0,0]), "00:00")



if __name__ == '__main__':
    unittest.main()
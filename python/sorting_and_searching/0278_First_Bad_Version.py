'''
01/05/2020

278. First Bad Version - Easy

Tag: Binary Search

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(nlogn)
    Space complexity : O(1)
    '''
    def firstBadVersion(self, n, bad):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            mid = l + (r-l) // 2
            if mid >= bad:
                r = mid - 1
            else:
                l = mid + 1
            
        return l

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.firstBadVersion
            self.assertEqual(func(5,4), 4)

if __name__ == '__main__':
    unittest.main()
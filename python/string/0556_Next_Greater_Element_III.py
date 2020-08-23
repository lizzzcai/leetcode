'''
23/08/2020

556. Next Greater Element III - Medium

Tag: String

Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21
 

Example 2:

Input: 21
Output: -1
 

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def nextGreaterElement(self, n: int) -> int:

        arr = []
        while n:
            remain = n % 10
            n //= 10
            arr.append(remain)
        
        arr = arr[::-1]
        
        n  = len(arr)
        i = n-2
        # find the first item from right that is decrease
        while i>=0 and arr[i] >= arr[i+1]:
            i-=1
            
        # return if cannot find
        if i == -1:
            return -1
        
        # find the first item from right that is greater than arr[i]
        j = n-1
        while j >= 0 and arr[i] >= arr[j]:
            j -= 1
        
        # swap i and j
        arr[i], arr[j] = arr[j], arr[i]
        
        # reverse the arr[i+1:]
        i = i+1
        j = n-1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        
        ans = 0
        for x in arr:
            ans = ans * 10 + x
        
        if ans <= 2**31-1:
            return ans
        return -1
        
            
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.nextGreaterElement
            self.assertEqual(func(11), -1)
            self.assertEqual(func(21), -1)
            self.assertEqual(func(12443322), 13222344)
            self.assertEqual(func(1999999999), -1)


if __name__ == '__main__':
    unittest.main()
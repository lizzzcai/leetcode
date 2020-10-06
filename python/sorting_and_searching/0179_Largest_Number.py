'''
25/09/2020

179. Largest Number - Easy

Tag: Sort

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.

'''

from typing import List
import functools
# Solution
class Solution1:
    '''
    Time complexity : O(nlogn)
    Space complexity : O(n)
    '''
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            a, b = x+y, y+x
            if a < b:
                return 1
            elif a > b:
                return -1
            
            return 0
        
        strs = [str(num) for num in nums]
        ans = "".join(sorted(strs, key=functools.cmp_to_key(compare)))
        
        if ans[0] == "0":
            return "0"
        
        return ans

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.largestNumber
            self.assertEqual(func([10,2]), "210")
            self.assertEqual(func([3,30,34,5,9]), "9534330")
            self.assertEqual(func([0,0]), "0")
            self.assertEqual(func([999999998,999999997,999999999]), "999999999999999998999999997")


if __name__ == '__main__':
    unittest.main()
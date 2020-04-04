'''
05/04/2020

263. Ugly Number - Easy

Tag: Math

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].

'''

from typing import List
# Solution
class Solution1:
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        if num == 1:
            return True

        if num % 2 == 0:
            return self.isUgly(num // 2)
        elif num % 3 == 0:
            return self.isUgly (num // 3)
        elif num % 5 == 0:
            return self.isUgly(num // 5)
        else:
            return False
            
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.isUgly
            self.assertEqual(func(6), True)
            self.assertEqual(func(8), True)
            self.assertEqual(func(14), False)
            self.assertEqual(func(1), True)
            self.assertEqual(func(0), False)
            self.assertEqual(func(-1), False)


if __name__ == '__main__':
    unittest.main()
'''
07/07/2020

66. Plus One - Easy

Tag: Array

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            x = digits[i]
            if carry:
                x += 1
                if x == 10:
                    x = 0
                else:
                    carry = 0
                digits[i] = x
                if not carry:
                    break
        
        if carry:
            return [1] + digits
        
        return digits
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.plusOne
            self.assertEqual(func([1,2,3]), [1,2,4])
            self.assertEqual(func([4,3,2,1]), [4,3,2,2])


if __name__ == '__main__':
    unittest.main()
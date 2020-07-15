'''
14/07/2020

1344. Angle Between Hands of a Clock - Medium

Tag: Math

Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

 

Example 1:



Input: hour = 12, minutes = 30
Output: 165
Example 2:



Input: hour = 3, minutes = 30
Output: 75
Example 3:



Input: hour = 3, minutes = 15
Output: 7.5
Example 4:

Input: hour = 4, minutes = 50
Output: 155
Example 5:

Input: hour = 12, minutes = 0
Output: 0
 

Constraints:

1 <= hour <= 12
0 <= minutes <= 59
Answers within 10^-5 of the actual value will be accepted as correct.
'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(1)
    Space complexity : O(1)
    '''
    def angleClock(self, hour: int, minutes: int) -> float:
        
        # convert hour to minutes also, and turn to zero if at 12
        h = hour / 12 * 360 % 360
        delta = minutes / 60 * 360 / 12
        m = minutes / 60 * 360

        ans = abs(h+delta - m)

        return ans if ans < 180 else 360 - ans


class Solution2:
    '''
    https://leetcode.com/problems/angle-between-hands-of-a-clock/discuss/735395/Python-math-solution-%2B-Oneliner-explained
    Time complexity : O(1)
    Space complexity : O(1)
    '''
    def angleClock(self, hour: int, minutes: int) -> float:
        
        # convert hour to minutes also, and turn to zero if at 12
        h = hour * 30 + 0.5 * minutes
        m = 6*minutes
        ans = abs(h - m)

        return ans if ans <= 180 else 360 - ans




# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.angleClock
            self.assertEqual(func(12,30), 165.0)
            self.assertEqual(func(3,30), 75.0)
            self.assertEqual(func(1,57), 76.5)



if __name__ == '__main__':
    unittest.main()
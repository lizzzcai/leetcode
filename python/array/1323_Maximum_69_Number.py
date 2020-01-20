'''
20/01/2020

1323. Maximum 69 Number - Easy

Tag: Math, String

Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 

Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666. 
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
 

Constraints:

1 <= num <= 10^4
num's digits are 6 or 9.

'''

from typing import List
# Solution
class Solution:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        for i in range(len(s)):
            if s[i] == '6':
                s = s[:i] + '9' + s[i+1:]
                break
        return int(s)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().maximum69Number
        self.assertEqual(func(9669), 9969)
        self.assertEqual(func(9696), 9999)
        self.assertEqual(func(9999), 9999)



if __name__ == '__main__':
    unittest.main()
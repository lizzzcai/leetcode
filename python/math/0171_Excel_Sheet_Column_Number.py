'''
11/08/2020

171. Excel Sheet Column Number - Easy

Tag: Math

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
 

Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for i, x in enumerate(s[::-1]):
            ans += (ord(x) - ord("A") + 1) * 26**i
        
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
            func = Sol.titleToNumber
            self.assertEqual(func("A"), 1)
            self.assertEqual(func("AB"), 28)
            self.assertEqual(func("ZY"), 701)


if __name__ == '__main__':
    unittest.main()
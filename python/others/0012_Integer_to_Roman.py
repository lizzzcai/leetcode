"""
15/09/2019
12. Integer to Roman - Medium
Tag: Other

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""

from typing import List
class Solution:
    def intToRoman(self, num: int) -> str:

        #strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        #nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]     
        Rmap = {
            1000:'M',
            900:'CM',
            500:'D',
            400:'CD',
            100:'C',
            90:'XC',
            50:'L',
            40:'XL',
            10:'X',
            9:'IX',
            5:'V',
            4:'IV',
            1:'I'
        }

        ret = ""
        # keep the order of Rmap from large to small, iteratively compare
        for n, r in Rmap.items():
            while num >= n:
                ret += r
                num -= n
            if num == 0:
                return ret

# Unit Test
import unittest
class intToRomanCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_intToRoman(self):
        func = Solution().intToRoman

        self.assertEqual(func(3), "III")
        self.assertEqual(func(4), "IV") 
        self.assertEqual(func(9), "IX")
        self.assertEqual(func(1994), "MCMXCIV")
        self.assertEqual(func(58), "LVIII")









if __name__ == '__main__':
    unittest.main()



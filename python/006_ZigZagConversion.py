"""
24/12/2018

Tag: Array

6. ZigZag Conversion - Medium


The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


'''
The distribution of the elements is period.

P   A   H   N
A P L S I I G
Y   I   R
For example, the following has 4 periods(cycles):

P   | A   | H   | N
A P | L S | I I | G
Y   | I   | R   |
The size of every period is defined as "cycle"

cycle = (2*nRows - 2), except nRows == 1.
In this example, (2*nRows - 2) = 4.

In every period, every row has 2 elements, except the first row and the last row.

Suppose the current row is i, the index of the first element is j:

j = i + cycle*k, k = 0, 1, 2, ...
The index of the second element is secondJ:

secondJ = (j - i) + cycle - i
(j-i) is the start of current period, (j-i) + cycle is the start of next period.

string convert(string s, int nRows) {
        if(nRows <= 1) return s;
        string result = "";
        //the size of a cycle(period)
        int cycle = 2 * nRows - 2;
        for(int i = 0; i < nRows; ++i)
        {
            for(int j = i; j < s.length(); j = j + cycle){
               result = result + s[j];
               int secondJ = (j - i) + cycle - i;
               if(i != 0 && i != nRows-1 && secondJ < s.length())
                   result = result + s[secondJ];
            }
        }
        return result;
    }
'''

class Solution:
    """
    Visit by Row
    Time Complexity: O(n), where n == len(s). Each index is visited once.

    Space Complexity: O(n). For the cpp implementation, O(1) if return string is not considered extra space.
    """

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        res = ""
        # length of input s
        strLen = len(s)
        # the size of every period (how many char)
        cycleLen = 2 * numRows - 2
        for i in range(numRows):
            '''
            for inner rows,
            first J:  k * cycleLen + i
            second J: (k+1) * cycleLen - i
            '''
            # make sure j + i < strLen
            for j in range(0, strLen - i, cycleLen): # j is the begining of each cycle period , except the last period
                res += s[j + i] # i is the row idx
                # for the inner rows (not beginning and end rows), find the second J
                # make sure j + cycleLen - i < strLen
                if (i != 0) and (i != numRows - 1) and (j + cycleLen - i < strLen):
                    res += s[j + cycleLen - i]
        return res


        
# Unit Test
import unittest
class ZigZagConversionCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ZigZagConversion(self):
        # SOLUTION 0
        func = Solution().convert
        self.assertEqual(func("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(func("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
        self.assertEqual(func("PAYPALISHIRING", 1),"PAYPALISHIRING")



if __name__ == '__main__':
    unittest.main()

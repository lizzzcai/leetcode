
'''
13/08/2020

119. Pascal's Triangle II - Easy

Tag: Array

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        row = [1,1]
        if rowIndex == 1:
            return row
        
        for _ in range(2, rowIndex+1):
            nxt = [row[j]+row[j+1] for j in range(len(row)-1)]
            row = [1] + nxt + [1]
        
        return row


class Solution2:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        row = [0]*(rowIndex+1)
        row[0]= 1
        for i in range(1, rowIndex+1):
            for j in range(i, 0,-1):
                row[j] += row[j-1]

        return row
 
                

# Unit Test
import unittest
class Testcase(unittest.TestCase):
    def test(self):
        for sol in [Solution1(), Solution2()]:
            func = sol.getRow
            self.assertEqual(func(3), [1,3,3,1])



if __name__ == '__main__':
    unittest.main()
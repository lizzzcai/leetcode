'''
22/08/2020

905. Sort Array By Parity - Easy

Tag: Array

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        j = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                j += 1
        
        return A
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.sortArrayByParity
            self.assertEqual(func([3,1,2,4]), [2,4,3,1])

if __name__ == '__main__':
    unittest.main()
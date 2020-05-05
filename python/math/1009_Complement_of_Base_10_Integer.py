'''
04/05/2020

1009. Complement of Base 10 Integer - Easy

Tag: Math

Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.

 

Example 1:

Input: 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
Example 2:

Input: 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
Example 3:

Input: 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
 

Note:

0 <= N < 10^9
This question is the same as 476: https://leetcode.com/problems/number-complement/

'''

from typing import List
# Solution
class Solution1:
    def bitwiseComplement(self, N: int) -> int:
        
        n = len(bin(N))-2
        return int('1'*n, 2) ^ N



class Solution2:
    def bitwiseComplement(self, N: int) -> int:
        
        if N == 0:
            return 1
        
        
        # get the binary 10000 which length is 1 bit larger than N
        # if N is 101, i= 1000 if 1, 10
        i = 1
        while i <= N:
            i <<= 1
        # i-1 to get 111 from 1000, 1 from 10
        # perform the XOR
        return (i-1)^N

class Solution3:
    def bitwiseComplement(self, N: int) -> int:
        
        X = 1
        while X < N:
            X = X*2+1
        return X-N

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(), Solution3()]:
            func = Sol.bitwiseComplement
            self.assertEqual(func(5), 2)
            self.assertEqual(func(7), 0)
            self.assertEqual(func(10), 5)
            self.assertEqual(func(0), 1)

if __name__ == '__main__':
    unittest.main()
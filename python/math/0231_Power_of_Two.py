'''
22/02/2020

231. Power of Two - Easy

Tag: Math, Bit Manipulation

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false


'''

# Solution

class Solution0:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        Time complexity = O(log n)
        '''
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1

class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n % 2 == 0:
            return self.isPowerOfTwo(n / 2)
        
        return n == 1

class Solution2:
    '''
    https://leetcode.com/problems/power-of-two/discuss/63966/4-different-ways-to-solve-Iterative-Recursive-Bit-operation-Math


    If n is the power of two:

    n = 2 ^ 0 = 1 = 0b0000...00000001, and (n - 1) = 0 = 0b0000...0000.
    n = 2 ^ 1 = 2 = 0b0000...00000010, and (n - 1) = 1 = 0b0000...0001.
    n = 2 ^ 2 = 4 = 0b0000...00000100, and (n - 1) = 3 = 0b0000...0011.
    n = 2 ^ 3 = 8 = 0b0000...00001000, and (n - 1) = 7 = 0b0000...0111.
    we have n & (n-1) == 0b0000...0000 == 0

    Otherwise, n & (n-1) != 0.


    '''
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0

class Solution3:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        O(1)
        '''
        # 2^30 max power of 2. 2^30 = 1073741824
        return n > 0 and 1073741824 % n == 0


class Solution4:
    def isPowerOfTwo(self, n: int) -> bool:
        # 2Very intuitive. If n is the power of 2, the bit count of n is 1.
        return n > 0 and bin(n).count("1") == 1

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for s in [Solution0(), Solution1(), Solution2(), Solution3(), Solution4()]:
            func = s.isPowerOfTwo
            self.assertEqual(func(0), False)
            self.assertEqual(func(1), True)
            self.assertEqual(func(2), True)
            self.assertEqual(func(16), True)
            self.assertEqual(func(218), False)

if __name__ == '__main__':
    unittest.main()
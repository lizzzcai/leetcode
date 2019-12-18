'''
18/12/2019

201. Bitwise AND of Numbers Range- Medium

Tag: Bit Manipulation

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0

'''

# Solution
class Solution:
    '''
    https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56719/JavaPython-easy-solution-with-explanation

    1.last bit of (odd number & even number) is 0.
    2.when m != n, There is at least an odd number and an even number, so the last bit position result is 0.
    3.Move m and n right a position.
    Keep doing step 1,2,3 until m equal to n, use a factor to record the iteration time.
    '''
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        zeros = 0
        while m < n: # or m != n
            m >>= 1
            n >>= 1
            zeros += 1
        return m << zeros
        

# Unit Test
import unittest
class rangeBitwiseAndCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_rangeBitwiseAndCase(self):
        func = Solution().rangeBitwiseAnd
        self.assertEqual(func(5, 7), 4)
        self.assertEqual(func(0, 1), 0)
        self.assertEqual(func(1, 1), 1)
        self.assertEqual(func(5, 2147483647), 0)
        self.assertEqual(func(2147483647, 2147483647), 2147483647)



if __name__ == '__main__':
    unittest.main()
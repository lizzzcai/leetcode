'''
06/07/2020

461. Hamming Distance - Easy

Tag: Bit Manupulation

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(32)
    Space complexity : O(1)
    '''
    def hammingDistance(self, x: int, y: int) -> int:
        a = x^y
        count = 0
        while a:
            if (a&1):
                count += 1
            a >>= 1
        
        return count

class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.hammingDistance
            self.assertEqual(func(1,4), 2)
            self.assertEqual(func(11,100), 6)


if __name__ == '__main__':
    unittest.main()
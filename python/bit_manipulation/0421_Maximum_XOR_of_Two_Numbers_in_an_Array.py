'''
16/09/2020

421. Maximum XOR of Two Numbers in an Array - Medium

Tag: Bit Manipulation, Trie

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

'''

from typing import List
# Solution
class Solution1:
    def findMaximumXOR(self, nums: List[int]) -> int:
        '''
        https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/91049/Java-O(n)-solution-using-bit-manipulation-and-HashMap
        O(n)
        '''
        max_result, mask = 0, 0
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            hset = set()
            for num in nums:
                num_left = num & mask
                hset.add(num_left)
            
            try_greedy = max_result | (1 << i)
            for num_left in hset:
                num_right = num_left ^ try_greedy
                if num_right in hset:
                    max_result = try_greedy
                    break
        
        return max_result
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.findMaximumXOR
            self.assertEqual(func([3, 10, 5, 25, 2, 8]), 28)

if __name__ == '__main__':
    unittest.main()
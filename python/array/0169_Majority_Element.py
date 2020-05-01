'''
01/05/2020

169. Majority Element - Easy

Tag: Array， Divide and Conquer, Bit Manipulation

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

from typing import List
# Solution
class Solution1:
    '''
    Boyer-Moore Majority Vote
    https://leetcode.com/problems/majority-element-ii/discuss/63537/My-understanding-of-Boyer-Moore-Majority-Vote
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for x in nums:
            if count == 0:
                res = x
            if res == x:
                count += 1
            else:
                count -= 1
        
        return res


class Solution2:
    '''
    Bit manipulation
    https://leetcode.com/problems/majority-element/discuss/51611/Java-solutions-(sorting-hashmap-moore-voting-bit-manipulation).
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def majorityElement(self, nums: List[int]) -> int:
        def convert(x):
            if x >= 2**31:
                x -= 2**32
            return x

        n = len(nums)
        bit = [0]*32
        for x in nums:
            for i in range(32):
                if (x >> (31-i) & 1) == 1:
                    bit[i] += 1

        res = 0
        for i in range(32):
            bit[i] = 1 if bit[i] > n / 2 else 0
            res += bit[i] * (1 << (31-i))

        return convert(res)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.majorityElement
            self.assertEqual(func([3,2,3]), 3)
            self.assertEqual(func([1,1,1,3,3,2,2,2]), 2)
            self.assertEqual(func([0,0,0]), 0)
            self.assertEqual(func([-2147483648]), -2147483648)


if __name__ == '__main__':
    unittest.main()
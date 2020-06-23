'''
01/06/2020

60. Permutation Sequence - Medium

Tag: Math, Backtracking

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
'''

from typing import List
# Solution
import math
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n+1))
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            idx, k = divmod(k, math.factorial(n))
            permutation += str(numbers[idx])
            numbers.remove(numbers[idx])
        return permutation

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.getPermutation
            self.assertEqual(func(3, 3), "213")
            self.assertEqual(func(4, 9), "2314")


if __name__ == '__main__':
    unittest.main()
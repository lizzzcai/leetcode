'''
28/05/2020

338. Counting Bits - Medium

Tag: Dynamic Programming, Bit Manipulation

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n*sizeof(int))
    Space complexity : O(n)
    '''
    def countBits(self, num: int) -> List[int]:
        res = []
        for x in range(num+1):
            count = 0
            while x:
                if x & 1 == 1:
                    count += 1
                x >>= 1
            res.append(count)
        return res

class Solution2:
    '''
    Time complexity : O(n*sizeof(int))
    Space complexity : O(n)
    '''
    def countBits(self, num: int) -> List[int]:
        res = [0]*(num+1)
        for x in range(1, num+1):
            res[x] = res[x >> 1] + (x & 1)
        return res

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.countBits
            self.assertEqual(func(2), [0, 1,1])
            self.assertEqual(func(5), [0, 1,1,2,1,2])


if __name__ == '__main__':
    unittest.main()
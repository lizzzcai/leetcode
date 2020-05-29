'''
28/05/2020

961. N-Repeated Element in Size 2N Array - Easy

Tag: Hash Table

In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5
 

Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def repeatedNTimes(self, A: List[int]) -> int:
        count = set()
        for x in A:
            if x in count:
                return x
            else:
                count.add(x)
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.repeatedNTimes
            self.assertEqual(func([1,2,3,3]), 3)
            self.assertEqual(func([2,1,2,5,3,2]), 2)
            self.assertEqual(func([5,1,5,2,5,3,5,4]), 5)



if __name__ == '__main__':
    unittest.main()
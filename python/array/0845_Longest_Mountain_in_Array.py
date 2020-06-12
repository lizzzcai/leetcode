'''
11/06/2020

845. Longest Mountain in Array - Medium

Tag: Two Pointers

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def longestMountain(self, A: List[int]) -> int:
        N = len(A)
        left = 0
        ans = 0
        while left < N:
            right = left
            # check if left is the left boundary
            if right + 1 < N and A[right] < A[right+1]:
                # move right to find the peak
                while right + 1 < N and A[right] < A[right+1]:
                    right += 1
                
                # check if right is a peak
                if right + 1 < N and A[right] > A[right+1]:
                    # move right to the right boundary
                    while right + 1 < N and A[right] > A[right+1]:
                        right += 1
                    
                    # update result
                    ans = max(ans, right-left+1)
            
            left = max(left+1, right)
            
        return ans
                    

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.longestMountain
            self.assertEqual(func([2,1,4,7,3,2,5]), 5)
            self.assertEqual(func([2,2,2]), 0)


if __name__ == '__main__':
    unittest.main()
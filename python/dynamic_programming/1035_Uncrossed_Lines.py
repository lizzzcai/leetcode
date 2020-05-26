'''
26/05/2020

1035. Uncrossed Lines - Medium

Tag: Array, Dynamic Programming

We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

 

Example 1:


Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2
 

Note:

1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000

'''

from typing import List
# Solution
class Solution1:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        '''
        dynamic programming
        The Longest Common Subsequence

        time: O(mn)
        Space: O(mn)
        '''
        
        dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]
        
        for i in range(len(A)):
            for j in range(len(B)):
                dp[i+1][j+1] = max(dp[i][j] + (A[i]==B[j]), dp[i+1][j], dp[i][j+1])
        
        return dp[len(A)][len(B)]


class Solution2:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        '''
        recurrsion
        The Longest Common Subsequence

        time: O(mn)
        Space: O(mn)
        '''
        memo = {}
        def helper(i, j, memo):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i == -1 or j == -1:
                return 0
            elif A[i] == B[j]:
                memo[(i, j)] = helper(i-1, j-1, memo) + 1
                return memo[(i, j)]
            else:
                memo[(i, j)] = max(helper(i, j-1, memo), helper(i-1, j, memo))
                return memo[(i, j)]
        
        return helper(len(A)-1, len(B)-1, memo)



# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.maxUncrossedLines
            self.assertEqual(func([1,4,2], [1,2,4]), 2)
            self.assertEqual(func([2,5,1,2,5], [10,5,2,1,5,2]), 3)
            self.assertEqual(func([1,3,7,1,7,5], [1,9,2,5,1]), 2)
            self.assertEqual(func([2,1], [1,2,1,3,3,2]), 2)
            self.assertEqual(func([1,1,3,5,3,3,5,5,1,1], [2,3,2,1,3,5,3,2,2,1]), 5)


if __name__ == '__main__':
    unittest.main()
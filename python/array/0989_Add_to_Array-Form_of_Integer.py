'''
24/12/2019

989. Add to Array-Form of Integer - Easy

Tag: String, Array

For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

 

Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
Example 4:

Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000
 

Note：

1 <= A.length <= 10000
0 <= A[i] <= 9
0 <= K <= 10000
If A.length > 1, then A[0] != 0


'''

from typing import List
# Solution
class Solution:
    '''
    Time complexity : O(max(m,n))
    Space complexity : O(max(m,n))
    '''
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        B = [int(x) for x in str(K)]
        m, n = len(A)-1, len(B)-1
        res = []
        carry = 0
        while m >= 0 or n >= 0:
            val_A = A[m] if m >= 0 else 0
            val_B = B[n] if n >= 0 else 0
            add = val_A + val_B
            carry, remain = divmod(add + carry, 10)
            res.append(remain)
            # move to next value
            m -= 1
            n -= 1
        if carry:
            res.append(carry)
        # reverse and return
        return res[::-1]
            
            

# Unit Test
import unittest
class addToArrayFormCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_addToArrayFormCase(self):
        func = Solution().addToArrayForm
        self.assertEqual(func([1,2,0,0], 34), [1,2,3,4])
        self.assertEqual(func([2,7,4], 181), [4,5,5])
        self.assertEqual(func([2,1,5], 806), [1,0,2,1])
        self.assertEqual(func([9,9,9,9,9,9,9,9,9,9], 1), [1,0,0,0,0,0,0,0,0,0,0])


if __name__ == '__main__':
    unittest.main()
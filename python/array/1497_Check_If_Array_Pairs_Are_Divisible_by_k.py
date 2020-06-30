'''
30/06/2020

1497. Check If Array Pairs Are Divisible by k - Medium

Tag: Array, Math, Greedy

Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return True If you can find a way to do that or False otherwise.

 

Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).
Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
Example 4:

Input: arr = [-10,10], k = 2
Output: true
Example 5:

Input: arr = [-1,1,-2,2,-3,3,-4,4], k = 3
Output: true
 

Constraints:

arr.length == n
1 <= n <= 10^5
n is even.
-10^9 <= arr[i] <= 10^9
1 <= k <= 10^5
'''

from typing import List
import collections
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) % 2 != 0:
            return False
        
        hmap = collections.defaultdict(int)
        count = 0
        for x in arr:
            key = k - x % k

            if key in hmap and hmap[key] > 0:
                count += 1
                hmap[key] -= 1
            else:
                # x % k in range [0, k-1], k-x%k in range [1, k]
                # in order to match the range, when x % k == 0, we should use k instead
                hmap[(x % k) or k] += 1
        
        
        return count == (len(arr) // 2)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.canArrange
            self.assertEqual(func([1,2,3,4,5,10,6,7,8,9], 5), True)
            self.assertEqual(func([1,2,3,4,5,6], 7), True)
            self.assertEqual(func([1,2,3,4,5,6], 10), False)
            self.assertEqual(func([1,2,3,4,5,6], 10), False)
            self.assertEqual(func([-10, 10], 2), True)





if __name__ == '__main__':
    unittest.main()
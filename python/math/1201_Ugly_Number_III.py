'''
05/04/2020

1201. Ugly Number III - Medium

Tag: Math, Binary Search

Write a program to find the n-th ugly number.

Ugly numbers are positive integers which are divisible by a or b or c.

 

Example 1:

Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
Example 2:

Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
Example 3:

Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
Example 4:

Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
Output: 1999999984
 

Constraints:

1 <= n, a, b, c <= 10^9
1 <= a * b * c <= 10^18
It's guaranteed that the result will be in range [1, 2 * 10^9]

'''

from typing import List
# Solution
class Solution1:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b, a%b)
        
        def lcm(a,b):
            return (a * b)//gcd(a,b)
        
        '''
        F(N) = a + b + c - a ∩ c - a ∩ b - b ∩ c + a ∩ b ∩ c
        F(N) = N/a + N/b + N/c - N/lcm(a, c) - N/lcm(a, b) - N/lcm(b, c) + N/lcm(a, b, c)(lcm = least common multiple)
        '''
        
        ac = lcm(a,c)
        ab = lcm(a,b)
        bc = lcm(b,c)
        abc = lcm(a,bc)
        
        l, r = 2, 2e9
        
        while l <= r:
            mid = l + (r-l) // 2
            # F(N) = (total number of positive integers <= N which are divisible by a or b or c.).
            # Find the least integer N that satisfies the condition F(N) >= K
            cnt = mid//a + mid//b + mid//c - mid//ac - mid//ab - mid//bc + mid//abc
            if cnt < n:
                l = mid + 1
            else:# cnt >= n
                r = mid - 1

        return int(l)
                



# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.nthUglyNumber
            self.assertEqual(func(3,2,3,5), 4)
            self.assertEqual(func(4,2,3,4), 6)
            self.assertEqual(func(5,2,11,13), 10)
            self.assertEqual(func(1000000000,2,217983653,336916467), 1999999984)



if __name__ == '__main__':
    unittest.main()
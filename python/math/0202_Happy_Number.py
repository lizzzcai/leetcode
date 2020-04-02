'''
02/04/2020

202. Happy Number - Easy

Tag: Math, Hash Table

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def isHappy(self, n: int) -> bool:
        check = set()
        
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in check:
                return False
            else:
                check.add(n)
        
        return True

class Solution2:
    def isHappy(self, n: int) -> bool:
        check = set()
        
        while n not in check:
            check.add(n)
            n = sum(int(i)**2 for i in str(n))
            if n == 1:
                return True
        
        return False
            
class Solution3:
    def isHappy(self, n: int) -> bool:
        check = set()
        while n not in check:
            check.add(n)
            nxt = 0
            while n:
                nxt += (n % 10)**2
                n //= 10
            n = nxt

            if n == 1:
                return True
        
        return False

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(), Solution3()]:
            func = Sol.isHappy
            self.assertEqual(func(19), True)
            self.assertEqual(func(7), True)
            self.assertEqual(func(11), False)


if __name__ == '__main__':
    unittest.main()
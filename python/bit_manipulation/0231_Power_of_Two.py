'''
23/02/2020

231. Power of Two - Easy

Tag: Bit Manipulation, Math

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false

'''

class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        if not n:
            return False
        
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                return False
        
        return True
        


class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        Power of 2 means only one bit of n is '1', so use the trick n&(n-1)==0 to judge whether that is the case
        '''
        if n <= 0:
            return False
        return (n&(n-1)) == 0
        
        
    

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for s in [Solution1(), Solution2()]:
            func = s.isPowerOfTwo
            self.assertEqual(func(0), False)
            self.assertEqual(func(1), True)
            self.assertEqual(func(2), True)
            self.assertEqual(func(16), True)
            self.assertEqual(func(218), False)
            self.assertEqual(func(5), False)
            self.assertEqual(func(4), True)



if __name__ == '__main__':
    unittest.main()
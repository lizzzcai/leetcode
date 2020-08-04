'''
23/02/2020

342. Power of Four - Easy

Tag: Bit Manipulation

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

'''

class Solution1:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 0:
            return False
        if num % 4 == 0:
            return self.isPowerOfFour(num / 4)
        
        return num == 1


class Solution2:
    def isPowerOfFour(self, num: int) -> bool:
        '''
        https://leetcode.com/problems/power-of-four/discuss/80461/Python-one-line-solution-with-explanations
        
        '''
        #mask = sum([4**i for i in range(0, 16)])
        mask = 0
        for i in range(0, 16):
            mask ^= 4**i
            
        is_power_of_two = num & (num-1) == 0
        is_power_of_four = num & mask == num
        
        return num > 0 and is_power_of_two and is_power_of_four
        
class Solution3:
    def isPowerOfFour(self, num: int) -> bool:
        '''
        First,greater than 0.Second,only have one '1' bit in their binary notation,so we use x&(x-1) to delete the lowest '1',and if then it becomes 0,it prove that there is only one '1' bit.Third,the only '1' bit should be locate at the odd location
        '''
        x = 1
        for i in range(32):
            x <<= 1
            if i % 2 != 0:
                x |= 1
            
        return num != 0 and num &(num-1) == 0 and num & x == num



# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for s in [Solution1(), Solution2(), Solution3()]:
            func = s.isPowerOfFour
            self.assertEqual(func(0), False)
            self.assertEqual(func(1), True)
            self.assertEqual(func(2), False)
            self.assertEqual(func(16), True)
            self.assertEqual(func(218), False)
            self.assertEqual(func(5), False)
            self.assertEqual(func(4), True)



if __name__ == '__main__':
    unittest.main()
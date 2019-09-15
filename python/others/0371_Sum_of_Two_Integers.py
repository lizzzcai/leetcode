"""
15/09/2019
371. Sum of Two Integers - Easy
Tag: Other, Bit manipulation

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        https://blog.csdn.net/coder_orz/article/details/52034541
        https://darktiantian.github.io/371-Sum-of-Two-Integers-Python/
        """
        MASK = 0xffffffff

        # in Python, every integer is associated with its two's complement and its sign.
        # However, doing bit operation "& mask" loses the track of sign. 
        # Therefore, after the while loop, a is the two's complement of the final result as a 32-bit unsigned integer. 
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # a is negative if the first bit is 1
        if (a >> 31) & 1:
            return ~(a ^ MASK)
        else:
            return a

# Unit Test
import unittest
class getSumCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getSum(self):
        func = Solution().getSum
 
        self.assertEqual(func(1, 2), 3)
        self.assertEqual(func(-2, 3), 1)
        self.assertEqual(func(2, -3), -1)
        self.assertEqual(func(-12, 8), -4)






if __name__ == '__main__':
    unittest.main()



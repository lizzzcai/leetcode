'''
05/02/2019

66. Plus One - Easy

Tag: Array

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''


class Solution:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        carry = False
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                carry = True
            else:
                digits[i] += 1
                carry = False
                break
        if carry:
            digits[:] = [1] + digits[:]
            #digits.insert(0, 1)
        return digits
        
class Solution2:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        tmp = ""
        for d in digits:
            tmp = tmp + str(d)
        print(tmp)
        print(int(tmp))
        num = str(int(tmp) + 1)
        print(num)
        return [int(d) for d in num]
                   

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().plusOne
        self.assertEqual(func([1,2,3,4]), [1,2,3,5])
        self.assertEqual(func([1,2,3,9]), [1,2,4,0])
        self.assertEqual(func([9]), [1,0])



if __name__ == '__main__':
    unittest.main()
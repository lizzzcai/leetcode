'''
25/12/2018

Tag: Binary Search

374. Guess Number Higher or Lower - Easy

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6
'''

def binarySearch(arr, target):
    left , right = 0, len(arr) - 1  
    while left <= right:            
        mid = (left+right)//2
        # mid = left + (right-left)//2 # avoid overflow
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1 
    return -1

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):



class Solution:
    '''
    Time Complexity: O(logn). 
    Space Complexity: O(1).
    '''
    def guessNumberRun(self, n, target):
        self.target = target
        result = self.guessNumber(n)
        return result

    def guess(self, guessNum):
        if guessNum == self.target:
            return 0
        elif guessNum >= self.target:
            return -1
        else: return 1

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            hint = self.guess(mid)
            if hint == 0:
                return mid
            elif hint == 1: # target higher than mine guess
                left = mid + 1
            else:           # target lower than mine guess 
                right = mid - 1
                

# Unit Test
import unittest
class TwoSumCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_twoSum(self):
        func = Solution().guessNumberRun
        self.assertEqual(func(10, 6), 6)

if __name__ == '__main__':
    unittest.main()
'''
17/04/2020

678. Valid Parenthesis String - Medium

Tag: 

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

from typing import List
# Solution
class Solution1:
    def checkValidString(self, s: str) -> bool:
        
        '''
        Greedy
        O(n)
        O(1)
        https://leetcode.com/problems/valid-parenthesis-string/discuss/302732/C%2B%2B-O(S)-Time-O(1)-Space-One-Pass-with-Explanation
        '''
        
        lo, hi = 0, 0
        for ch in s:
            if ch == '(':
                lo += 1
                hi += 1
            elif ch == ')':
                lo -= 1
                hi -= 1
            else:# *
                lo -= 1
                hi += 1
                
            if hi < 0: # invalid
                return False
            
            # lo < 0 is not allow during the process
            # if lo < 0, we can assume some of the * as ( t balance to 0, hi is not affected as the final result not depend on it
            # if hi < 0 even we assume all * as (, then result is invalid
            lo = max(lo, 0)
            
        return lo == 0
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.checkValidString
            self.assertEqual(func("()"), True)
            self.assertEqual(func("(*)"), True)
            self.assertEqual(func("(*))"), True)
            self.assertEqual(func(")("), False)
            self.assertEqual(func("(())((())()()(*)(*()(())())())()()((()())((()))(*"), False)

if __name__ == '__main__':
    unittest.main()
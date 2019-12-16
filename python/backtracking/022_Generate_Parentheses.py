'''
16/12/2019

22. Generate Parentheses - Medium

Tag: Backtracking

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''

from typing import List

# Solution
class Solution:
    '''
    Time complexity : O(4^n/sqrt(n))
    Space complexity : O(4^n/sqrt(n))
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        res = []
        self.helper(n, n, '', res)
        return res
    
    def helper(self, l, r, item, res):
        if r < l:
            return
        if r == 0 and l == 0:
            res.append(item)
        if l > 0:
            self.helper(l-1, r, item + '(', res)
        if r > 0:
            self.helper(l, r-1, item + ')', res)
        

# Unit Test
import unittest
class generateParenthesisCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generateParenthesisCase(self):
        func = Solution().generateParenthesis
        self.assertEqual(func(0), [""])
        self.assertEqual(func(-1), [])
        self.assertEqual(func(2), ["(())","()()"])
        self.assertEqual(func(3), ["((()))","(()())","(())()","()(())","()()()"])



if __name__ == '__main__':
    unittest.main()
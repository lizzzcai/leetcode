"""
22/09/2019
76. Minimum Window Substring - Hard
Tag: Array, sliding window

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # count the char and num in t
        dict_t = Counter(t)
        # required char to be show in the window
        required = len(dict_t)
        
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0
        
        # count the number of char inside window
        window_count = {}
        
        # result: (window_length, left, right)
        res = (len(s)+1, None, None)
        
        while r < len(s):
            # get the char at right
            char = s[r]
            # add it to the count
            window_count[char] = window_count.get(char, 0) + 1
            
            # if char in t and char in window meet the number required in t
            if char in dict_t and dict_t[char] == window_count[char]:
                formed += 1
            
            # if the window contain all the char in t, and l <= r,
            # l = r for the case that only one char in the s
            while formed == required and l <= r:
                # char to remove from window
                char = s[l]
                # remove from window count
                window_count[char] -= 1
                
                # check num of char in window meet the min requirement in t
                if char in dict_t and window_count[char] < dict_t[char]:
                    formed -= 1
                
                # update the ans if smaller than current result
                if r-l+1 < res[0]:
                    res = (r-l+1, l, r)
                # move left pointer a step further
                l += 1
            # move right pinter a step further            
            r+= 1
        
        # if len of window not change since begin, cannot find window contain all char in T
        if res[0] == len(s) + 1:
            return ""
        else:
            return s[res[1]:res[2]+1]
        
        
# Unit Test
import unittest
class minWindowCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_minWindow(self):
        func = Solution().minWindow
        self.assertEqual(func("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(func("a", "a"), "a")
        self.assertEqual(func("ADOBECODEBANC", "ABCZ"), "")
        self.assertEqual(func("ADOBECODEBANC", ""), "")
        self.assertEqual(func("", "ABCZ"), "")




if __name__ == '__main__':
    unittest.main()



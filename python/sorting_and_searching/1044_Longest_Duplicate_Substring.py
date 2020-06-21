'''
20/06/2020

1044. Longest Duplicate Substring - Hard

Tag: Binary Search, Hash Table

Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

 

Example 1:

Input: "banana"
Output: "ana"
Example 2:

Input: "abcd"
Output: ""
 

Note:

2 <= S.length <= 10^5
S consists of lowercase English letters.

'''

from typing import List
import collections
# Solution
class Solution1:
    def longestDupSubstring(self, S: str) -> str:
        
        def code(t):
            return ord(t) - ord('a')+1
        def check(length):
            seen = collections.defaultdict(list)
            
            MOD = 10 ** 9 + 7
            P = 113
            INV_P = pow(P, MOD-2, MOD)# x^y % z = P^(MOD-2) % MOD

            P = 113
            MOD = 10 ** 9 + 7
            INV_P = 1/113



            h = 0
            power = 1
            '''
            h1 = s[0]p^0+s[1]p^1+s[2]p^2 +...+s[length-1]p^(length-1)
            move next:
            h2 = s[1]p^0+s[2]p^1+s[3]p^2 +...+s[length]p^(length-1)
            
            h2 = (h1 - S[i-length+1])*INV_P % MOD
            
            '''
            for i, x in enumerate(S):
                h = (h + power*code(x)) % MOD 
                if i < length-1:
                    power = power * P % MOD
                else:
                    # start: i-(length-1)
                    if h in seen:
                        for j in seen[h]:
                            if S[i-(length-1):i+1] == S[j:j+length]:
                                return S[j:j+length], True
                    seen[h].append(i-(length-1))
                    h = (h-code(S[i-(length-1)]))*INV_P % MOD
            
            return '', False
        
        res = ''
        l, r = 1, len(S)-1
        while l <= r:
            mid = (l+r)//2
            sub, is_check = check(mid)
            if is_check:
                res = sub
                l = mid + 1
            else:
                r = mid - 1
        
        return res
        
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.longestDupSubstring
            self.assertEqual(func("banana"), "ana")
            self.assertEqual(func("abcd"), "")

if __name__ == '__main__':
    unittest.main()
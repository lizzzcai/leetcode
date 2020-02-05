'''
05/02/2020

1160. Find Words That Can Be Formed by Characters - Easy

Tag: Array, Hash Table

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
 

'''

from typing import List
# Solution
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = dict()
        n = len(chars)
        for ch in chars:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        
        res = 0
        for word in words:
            l = len(word)
            if l > n:
                continue
            copy = count.copy()
            done = True
            for c in word:
                if c not in copy or copy[c] == 0:
                    done = False
                    break                
                copy[c] -= 1

            if done:
                res += l
        
        return res
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().countCharacters
        self.assertEqual(func(["cat","bt","hat","tree"], "atach"), 6)
        self.assertEqual(func(["hello","world","leetcode"], "welldonehoneyr"), 10)


if __name__ == '__main__':
    unittest.main()
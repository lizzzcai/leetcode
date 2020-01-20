'''
06/01/2020

1324. Print Words Vertically - Medium

Tag: String

Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.

 

Example 1:

Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"
Example 2:

Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"
Example 3:

Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]
 

Constraints:

1 <= s.length <= 200
s contains only upper case English letters.
It's guaranteed that there is only one space between 2 words.

'''

from typing import List
# Solution
class Solution:
    def printVertically(self, s: str) -> List[str]:
        '''
        Time: O(N) N is the number of char
        Space: O(N)
        '''
        # split the string into words
        s = s.split(' ')
        
        # num of word in string
        num_word = len(s)

        # max len for the word
        max_len = 0
        for word in s:
            max_len = max(max_len, len(word))
        
        # result
        res = [[] for _ in range(max_len)]
        
        for idx, word in enumerate(s):
            for i, ch in enumerate(word):
                # fill the leading zero to make sure the char is in its location vertically
                if len(res[i]) < idx:
                    res[i] += [' ' for _ in range(idx - len(res[i]))]
                res[i].append(ch)
        
        res = [''.join(x) for x in res]
        return res

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().printVertically
        self.assertEqual(func("AA BBB C DDDD EEEEE F"), ["ABCDEF","AB DE"," B DE","   DE","    E"])
        self.assertEqual(func("HOW ARE YOU"), ["HAY","ORO","WEU"])
        self.assertEqual(func("TO BE OR NOT TO BE"), ["TBONTB","OEROOE","   T"])
        self.assertEqual(func("CONTEST IS COMING"), ["CIC","OSO","N M","T I","E N","S G","T"])



if __name__ == '__main__':
    unittest.main()
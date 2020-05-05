'''
05/05/2020

387. First Unique Character in a String - Easy

Tag: Hash Table, String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

'''

from typing import List
# Solution
class Solution1:
    def firstUniqChar(self, s: str) -> int:
        '''
        Time O(n)
        Space O(n)
        '''
        res = len(s)+1
        visited = {}
        for idx, ch in enumerate(s):
            if ch not in visited:
                visited[ch] = idx
            else:
                visited[ch] = -1
        
        for v in visited.values():
            if v >= 0 and v < res:
                res = v
        
        if res <= len(s):
            return res
        
        return -1

class Solution2:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx

        return -1

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.firstUniqChar
            self.assertEqual(func("leetcode"), 0)
            self.assertEqual(func("loveleetcode"), 2)
            self.assertEqual(func("cc"), -1)

if __name__ == '__main__':
    unittest.main()
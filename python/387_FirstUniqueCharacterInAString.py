'''
08/02/2019

387. First Unique Character in a String - Easy

Tag: String, hashmap

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

'''

# Solution
class Solution:
    '''
    Time complexity : O(n), since we go through the string of length N two times
    Space complexity : O(n), since we have to keep a hash map with N elements.
    '''
    def firstUniqChar(self, s: 'str') -> 'int':
        
        # build hash map : character and how often it appears
        # count = collections.Counter(s)
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        idx = 0
        for char in s:
            if count[char] == 1:
                return idx
            else:
                idx += 1
        
        return -1

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().firstUniqChar
        self.assertEqual(func("leetcode"), 0)
        self.assertEqual(func("loveleetcode"), 2)


if __name__ == '__main__':
    unittest.main()
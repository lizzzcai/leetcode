'''
08/02/2019

242. Valid Anagram - Easy

Tag: String, HashTable

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

# Solution
class Solution:
    '''
    Time complexity : O(n),  accessing the counter table is a constant time 
    Space complexity : O(1), Although we do use extra space, the space complexity is O(1) because the table's size stays constant no matter how large n is.


    '''
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        
        ls = len(s)
        lt = len(t)
        if lt != ls:
            return False
        # build hash map : character and how often it appears
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        for char in t:
            if char not in count:
                return False
            else:
                if count[char] > 0:
                    count[char] -= 1
                else:
                    return False
        
        # as ls must equal to lt, no need to check again the count
        return True
                
        
        
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().isAnagram
        self.assertEqual(func("anagram", "nagaram"), True)
        self.assertEqual(func("rat", "car"), False)
        self.assertEqual(func("ratt", "car"), False)



if __name__ == '__main__':
    unittest.main()
"""
19/12/2018

Tag: Hash Table, Set, Array

3. Longest Substring Without Repeating Characters - Medium


Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

# Using set
class Solution1:
    """
    Sliding Window

    Time complexity : O(2n)=O(n). In the worst case each character will be visited twice by i and j.

    Space complexity : O(min(m,n)). Same as the previous approach. We need O(k) space for the sliding window, where k is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the charset/alphabet m. 
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        HashSet = set()
        ans = 0
        i, j = 0, 0
        while (i < n and j < n):
            # try to extend the range [i, j]
            if (s[j] not in HashSet):
                HashSet.add(s[j])
                ans = max(ans, j - i + 1)
                j += 1
            else:
                HashSet.remove(s[i])
                i += 1
        return ans

class Solution:
    """
    Sliding Window Optimized
    
    Time complexity : O(n). Index j will iterate n times.

    Space complexity (HashMap) : O(min(m, n)). Same as the previous approach.

    Space complexity (Table): O(m). m is the size of the charset.
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        HashMap = {} # current index of character
        ans = 0
        i, j = 0, 0
        # try to extend the range [i, j]
        while (j < n):
            # if s[j] have a duplicate in the range [i, j) with index j'
            if (s[j] in HashMap):
                # we skip all the elements in range [i, j'] and let i to be j'+1
                i = max(HashMap[s[j]] + 1, i)
            ans = max(ans, j - i + 1)
            # assign j' here
            HashMap[s[j]] = j
            j += 1
        return ans



# Unit Test
import unittest
class lengthOfLongestSubstringCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_lengthOfLongestSubstring(self):
        func = Solution().lengthOfLongestSubstring
        self.assertEqual(func("abcabcbb"), 3)
        self.assertEqual(func("bbbbb"), 1)
        self.assertEqual(func("pwwkew"), 3)

if __name__ == '__main__':
    unittest.main()
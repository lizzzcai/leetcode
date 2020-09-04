'''
04/09/2020

1278. Palindrome Partitioning III - Hard

Tag: Dynamic Programming

You are given a string s containing lowercase letters and an integer k. You need to :

First, change some characters of s to other lowercase English letters.
Then divide s into k non-empty disjoint substrings such that each substring is palindrome.
Return the minimal number of characters that you need to change to divide the string.

 

Example 1:

Input: s = "abc", k = 2
Output: 1
Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.
Example 2:

Input: s = "aabbc", k = 3
Output: 0
Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.
Example 3:

Input: s = "leetcode", k = 8
Output: 0
 

Constraints:

1 <= k <= s.length <= 100.
s only contains lowercase English letters.
'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n^2*k)
    Space complexity : O(n*k)
    '''
    def palindromePartition(self, s: str, k: int) -> int:
        '''
        https://leetcode.com/problems/palindrome-partitioning-iii/discuss/441423/python-easy-dp-solution
        
        '''
        def num_changes(s):
            i, j = 0, len(s)-1
            count = 0
            while i < j:
                if s[i] != s[j]:
                    count += 1
                i+=1
                j-=1
            
            return count
        
        def dp(i, k, memo):
            if (i, k) in memo:
                return memo[(i,k)]
            
            if k == 1:
                memo[(i, k)] = num_changes(s[:i+1])
            else:
                memo[(i, k)] = min(dp(j, k-1, memo) + num_changes(s[j+1:i+1]) for j in range(k-2, i))
            return memo[(i, k)]
        
        memo = dict()
        return dp(len(s)-1, k, memo)

class Solution2:
    def partitionLabels(self, S: str) -> List[int]:
        '''
        O(N)
        O(1) space
        '''
        last = {c:i for i, c in enumerate(S)}
        start, j = 0, 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(j-start+1)
                start = i+1
        
        return ans     

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.palindromePartition
            self.assertEqual(func("abc", 2), 1)
            self.assertEqual(func("abbc", 3), 0)
            self.assertEqual(func("leetcode", 9), 0)


if __name__ == '__main__':
    unittest.main()
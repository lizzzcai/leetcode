'''
04/09/2020

763. Partition Labels - Medium

Tag: Two Pointers, Greedy

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(nlgn)
    Space complexity : O(n)
    '''
    def partitionLabels(self, S: str) -> List[int]:
        range_map = dict()
        for idx, c in enumerate(S):
            if c in range_map:
                range_map[c][1] = idx
            else:
                range_map[c] = [idx, idx]
        
        range_list = [x for x in range_map.values()]
        range_list.sort(key=lambda x:x[0])
        
        ans = []
        start, end = range_list[0]
        for x in range_list[1:]:
            # if overlap
            if x[0] <= end:
                end = max(x[1], end)
            else:
                ans.append(end-start+1)
                start, end = x[0], x[1]
        
        ans.append(end-start+1)
        
        return ans

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
            func = Sol.partitionLabels
            self.assertEqual(func("ababcbacadefegdehijhklij"), [9, 7, 8])

if __name__ == '__main__':
    unittest.main()
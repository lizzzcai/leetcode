'''
23/05/2020

451. Sort Characters By Frequency - Medium

Tag: Hash Table, Heap

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

'''

from typing import List
import collections
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def frequencySort(self, s: str) -> str:
        count = collections.Counter(s)
        count = sorted(count.items(), key=lambda kv: kv[1], reverse=True)
        res = ""
        for k, v in count:
            res += k*v
        
        return res

from heapq import heapify, heappop, heappush
class Solution2:
    def frequencySort(self, s: str) -> str:
        '''
        Heap
        
        Time: O(N+klog(N)). heapify and counting are O(N), each of k heappop are O(logN)
        Space: O(N)
        
        
        '''
        if len(s) < 3:
            return s
        
        # count the frequency of each char
        count = {}
        for ch in s:
            count[ch] = count.setdefault(ch, 0) + 1
        
        heap = [(-freq, ch) for ch, freq in count.items()]
        heapify(heap)
        
        res = ''
        while heap:
            freq, char = heappop(heap)
            res += char * (-freq)
        
        return res

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.frequencySort
            self.assertIn(func("tree"), ["eert", "eetr"])
            self.assertIn(func("cccaaa"), ["cccaaa", "aaaccc"])
            self.assertIn(func("Aabb"), ["bbAa", "bbaA"])


if __name__ == '__main__':
    unittest.main()
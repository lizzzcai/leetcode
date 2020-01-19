'''
18/01/2020

692. Top K Frequent Words - Medium

Tag: Array, Hash Table, Heap, Trie

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

'''

from typing import List
# Solution
class Solution1:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        Sorting
        
        Time: O(nlogn)
        Space: O(n)
        
        '''
        count = dict()
        for w in words:
            count[w] = count.setdefault(w, 0) + 1
        sorted_keys = [k for k in count.keys()]
        sorted_keys.sort(key= lambda w:(-count[w], w))
        return sorted_keys[:k]

from heapq import heapify, heappop
class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        Heap
        
        Time: O(N+klog(N)). heapify and counting are O(N), each of k heappop are O(logN)
        Space: O(N)
        
        '''
        count = dict()
        for w in words:
            count[w] = count.setdefault(w, 0) + 1
        # mini heap in python
        heap = [(-v, k) for k, v in count.items()]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution1().topKFrequent
        self.assertEqual(func(["i", "love", "leetcode", "i", "love", "coding"], 2), ["i","love"])
        self.assertEqual(func(["i", "love", "leetcode", "i", "love", "coding"], 3), ["i","love","coding"])
        self.assertEqual(func(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4), ["the", "is", "sunny", "day"])

        func = Solution2().topKFrequent
        self.assertEqual(func(["i", "love", "leetcode", "i", "love", "coding"], 2), ["i","love"])
        self.assertEqual(func(["i", "love", "leetcode", "i", "love", "coding"], 3), ["i","love","coding"])
        self.assertEqual(func(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4), ["the", "is", "sunny", "day"])


if __name__ == '__main__':
    unittest.main()
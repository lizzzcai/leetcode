'''
13/06/2020

691. Stickers to Spell Word - Hard

Tag: Dynamic Programming, Backtracking

We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given target string by cutting individual letters from your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target? If the task is impossible, return -1.

Example 1:

Input:

["with", "example", "science"], "thehat"
Output:

3
Explanation:

We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
Example 2:

Input:

["notice", "possible"], "basicbasic"
Output:

-1
Explanation:

We can't form the target "basicbasic" from cutting letters from the given stickers.
Note:

stickers has length in the range [1, 50].
stickers consists of lowercase English words (without apostrophes).
target has length in the range [1, 15], and consists of lowercase English letters.
In all test cases, all words were chosen randomly from the 1000 most common US English words, and the target was chosen as a concatenation of two random words.
The time limit may be more challenging than usual. It is expected that a 50 sticker test case can be solved within 35ms on average.

'''

from typing import List
import collections, math
# Solution
class Solution1:
    '''
    Time complexity : O(ST)
    Space complexity : O(ST)
    '''
    def minStickers(self, stickers: List[str], target: str) -> int:
        cnt, res, n = collections.Counter(target), math.inf, len(target)
        
        def dfs(count, used, i):
            nonlocal res
            # if reach the end
            if i == n:
                res = min(res, used)
            # if the stikers have enough number for all char target[i]
            elif count[target[i]] >= cnt[target[i]]:
                dfs(count, used, i+1)

                
            elif used + 1 < res:
                for sticker in stickers:
                    if target[i] in sticker:
                        for s in sticker: count[s] += 1
                        dfs(count, used+1, i+1)
                        for s in sticker: count[s] -= 1
        
        dfs(collections.defaultdict(int), 0, 0)
        
        return res if res != math.inf else -1
                
                

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.minStickers
            self.assertEqual(func(["with", "example", "science"], "thehat"), 3)
            self.assertEqual(func(["notice", "possible"], "basicbasic"), -1)


if __name__ == '__main__':
    unittest.main()
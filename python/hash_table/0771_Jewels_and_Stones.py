'''
01/05/2020

771. Jewels and Stones - Easy

Tag: Hash Table

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = {}
        for s in S:
            count[s] = count.get(s, 0) + 1
        
        return sum(count.get(j, 0) for j in J)



class Solution2:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jws = set(J)
        res = 0
        for s in S:
            if s in jws:
                res += 1
        return res

class Solution3:
    def numJewelsInStones(self, J: str, S: str) -> int:

        return sum(map(S.count, J)) 

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(),Solution3()]:
            func = Sol.numJewelsInStones
            self.assertEqual(func("aA", "aAAbbbb"), 3)
            self.assertEqual(func("z", "ZZ"), 0)

if __name__ == '__main__':
    unittest.main()
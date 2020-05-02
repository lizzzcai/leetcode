'''
02/05/2020

292. Nim Game - Easy

Tag: Brainteaser, Minimax

You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

Example:

Input: 4
Output: false 
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be 
             removed by your friend.

'''

from typing import List
# Solution
class Solution1:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.canWinNim
            self.assertEqual(func(4), False)

if __name__ == '__main__':
    unittest.main()
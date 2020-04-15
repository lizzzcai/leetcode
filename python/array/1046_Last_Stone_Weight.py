'''
04/04/2020

1046. Last Stone Weight - Easy

Tag: Heap, Greedy

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000

'''

from typing import List
import heapq
# Solution
class Solution1:
    '''
    Time complexity : O(nlogn)
    Space complexity : O(n)
    '''
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = []
        for x in stones:
            heapq.heappush(hq, -x)
        
        while len(hq) > 1:
            y = -heapq.heappop(hq)
            x = -heapq.heappop(hq)
            if x != y:
                y -= x
                heapq.heappush(hq, -y)
        
        if hq:
            return -heapq.heappop(hq)
        else:
            return 0


class Solution2:
    '''
    Time complexity : O(nlogn)
    Space complexity : O(n)
    '''
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = [-x for x in stones]
        heapq.heapify(hq)

        while len(hq) > 1 and hq[0]:
            heapq.heappush(hq, heapq.heappop(hq) - heapq.heappop(hq))

        return -hq[0]

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.lastStoneWeight
            self.assertEqual(func([2,7,4,1,8,1]), 1)

if __name__ == '__main__':
    unittest.main()
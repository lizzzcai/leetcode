'''
26/04/2020

1306. Jump Game III - Medium

Tag: BFS, Graph

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3
Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
 

Constraints:

1 <= arr.length <= 5 * 10^4
0 <= arr[i] < arr.length
0 <= start < arr.length
'''

from typing import List
# Solution
class Solution1:
    def canReach(self, arr: List[int], start: int) -> bool:
        '''
        BFS
        time: O(n)
        Space: O(n)
        '''
        visited = set()    
        stack = [start]
        while stack:
            curr_pos = stack.pop()
            if arr[curr_pos] == 0:
                return True
            if curr_pos not in visited:
                visited.add(curr_pos)
                if 0<= curr_pos + arr[curr_pos] < len(arr):
                    stack.append(curr_pos + arr[curr_pos])
                if 0<= curr_pos - arr[
                    curr_pos] < len(arr):
                    stack.append(curr_pos - arr[curr_pos])    

        return False


class Solution2:
    def canReach(self, arr: List[int], start: int) -> bool:
        '''
        Recursion
        time: O(n)
        Space: O(n)
        https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/discuss/446376/JavaC%2B%2BPython-Binary-Search
        '''

        if 0 <= start < len(arr) and arr[start] >= 0:
            arr[start] = -arr[start]
            return arr[start] == 0 or self.canReach(arr, start+arr[start]) or self.canReach(arr, start-arr[start])
        return False


import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.canReach
            self.assertEqual(func([4,2,3,0,3,1,2], 5), True)
            self.assertEqual(func([4,2,3,0,3,1,2], 0), True)
            self.assertEqual(func([3,0,2,1,2], 2), False)


if __name__ == '__main__':
    unittest.main()
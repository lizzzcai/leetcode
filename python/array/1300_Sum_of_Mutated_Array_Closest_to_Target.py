'''
08/01/2020

1300. Sum of Mutated Array Closest to Target - Medium

Tag: Array, Binary Search, Sort


Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.

 

Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
Example 2:

Input: arr = [2,3,5], target = 10
Output: 5
Example 3:

Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i], target <= 10^5
'''

from typing import List
# Solution
class Solution0:
    '''
    Time complexity : O(nlogn)
    Space complexity : O(1)
    '''
    def findBestValue(self, arr: List[int], target: int) -> int:
        '''
        
        a,b,c   D,E,F
        
        keep,   replace by v
        
        keep + v * num_replaced = target
        
        left:
        keep = sum - (D, E, F)
        right:
        v * num_replaced
        
        left + right = target
        
        '''
        # sort the arr in desending order
        arr.sort()
        
        num_replaced, last_idx = 0, len(arr) - 1
        s = 0 # sum
        for val in arr:
            s += val
        if s <= target:
            return  arr[-1]
        
        while last_idx >= 0 and target < s + num_replaced * arr[last_idx]:
            num_replaced += 1
            s -= arr[last_idx]
            last_idx -= 1
        
        v = (target - s) // num_replaced
        
        # v or v + 1
        if abs(target - s - num_replaced * v) <= abs(target - s - num_replaced * (v+1)):
            return v
        else:
            return v+1

# binary search
class Solution1:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        def _sum(mid):
            return sum([v if v <= mid else mid for v in arr])
        
        l, r = 0, max(arr)
        while l <= r:
            mid = l + (r-l)//2
            s = _sum(mid)
            if s == target:
                return mid
            if target > s:
                l = mid + 1
            else:
                r = mid - 1
                
        if abs(target - _sum(r)) <= abs(target - _sum(r+1)):
            return r
        else:
            return r+1
        
        
# sort and iterate
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        s, n = 0, len(arr)
        
        for i in range(n):
            ans = round((target - s)/(n-i))
            if ans <= arr[i]: return ans 
            s += arr[i]
            
        return arr[-1]



# Unit Test
import unittest
class findBestValueCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_findBestValueCase(self):
        func = Solution().findBestValue
        self.assertEqual(func([4,9,3], 10), 3)
        self.assertEqual(func([5,2,3], 10), 5)
        self.assertEqual(func([60864,25176,27249,21296,20204], 56803), 11361)



if __name__ == '__main__':
    unittest.main()
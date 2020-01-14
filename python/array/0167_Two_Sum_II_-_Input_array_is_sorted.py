'''
14/01/2020

167. Two Sum II - Input array is sorted - Easy

Tag: Array, Two Pointers, Binary Search, Hash Table

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

'''

from typing import List
# Solution
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Hash Table
        Time complexity : O(n)
        Space complexity : O(n)
        '''

        hmap = {}
        
        for i in range(len(numbers)):
            if numbers[i] in hmap:
                return [hmap[numbers[i]]+1, i+1]
            else:
                hmap[target-numbers[i]] = i

class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Two pointers
        Time complexity : O(n)
        Space complexity : O(1)
        '''
        
        left, right = 0, len(numbers)-1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1, right+1]
            elif s < target:
                left += 1
            else:
                right -= 1


class Solution3:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        binary search
        Time: O(nlogn)
        '''
        visited = set()
        for i in range(len(numbers)):
            if numbers[i] not in visited:
                visited.add(numbers[i])
                left, right = i+1, len(numbers)-1
                tmp = target - numbers[i]
                while left <= right:
                    mid = (left + right) // 2
                    if numbers[mid] == tmp:
                        return [i+1, mid+1]
                    elif numbers[mid] > tmp:
                        right = mid - 1
                    else:
                        left = mid + 1

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution1().twoSum
        self.assertEqual(func([2, 7, 11, 15], 9), [1, 2])
        func = Solution2().twoSum
        self.assertEqual(func([2, 7, 11, 15], 9), [1, 2])    
        func = Solution3().twoSum
        self.assertEqual(func([2, 7, 11, 15], 9), [1, 2])

if __name__ == '__main__':
    unittest.main()
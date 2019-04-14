'''
05/02/2019

350. Intersection of Two Arrays II - Easy

Tag: Array, hashset, binary search

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

# Solution
class Solution1:
    '''
    Sort and two pointers
    Time complexity : O(min(m,n))
    Space complexity : O(m+n)
    '''
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        
        return res

class Solution:
    '''
    Sort and two pointers
    Time complexity : O(m+n)
    Space complexity : O(m+n)
    '''
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        hashmap = dict()
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        for num in nums1:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        res = []
        for num in nums2:
            if num in hashmap and hashmap[num] > 0:
                res.append(num)
                hashmap[num] -= 1
        return res
                  

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().intersect
        self.assertEqual(func([1,2,2,1], [2,2]), [2,2])

if __name__ == '__main__':
    unittest.main()
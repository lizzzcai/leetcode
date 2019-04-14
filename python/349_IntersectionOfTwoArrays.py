'''
05/02/2019

349. Intersection of Two Arrays - Easy

Tag: Array, hashset, two pointer, binary search

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

- Each element in the result must be unique.
- The result can be in any order.
'''

# Solution
class Solution:
    '''
    Time complexity : O(max(m,n))
    Space complexity : O(max(m,n)+1)
    '''
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':

    # def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        if len(nums1) == 0 or len(nums2) == 0:
            return []
        set1 = set(nums1)
        set2 = set(nums2)
        n1 = len(set1)
        n2 = len(set2)
        if n1 > n2:
            set1, set2 = set2, set1
            n1, n2 = n2, n1
        res = []
        for _ in range(n1):
            i = set1.pop()
            if i in set2:
                res.append(i)
        return res

class Solution1:
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        hashset = set()
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                hashset.add(nums1[i])
                i += 1
                j += 1
        
        return list(hashset)
                 

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().intersection
        self.assertEqual(func([1,2,2,1], [2,2]), [2])

if __name__ == '__main__':
    unittest.main()
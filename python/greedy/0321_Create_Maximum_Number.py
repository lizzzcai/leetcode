'''
14/05/2020

321. Create Maximum Number - Hard

Tag: Dynamic Programming, Greedy

Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]
Example 2:

Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]
Example 3:

Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]

'''

from typing import List
# Solution


class Solution1:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        '''
        Worse case (m+n)^3
        '''
        def prepare(nums, k):
            drop = len(nums)-k
            q= []
            for x in nums:
                # mono queue keep it decreasing
                while drop and q and q[-1] < x:
                    q.pop()
                    drop -= 1
                q.append(x)
            
            return q[:k]
        
        def merge(nums1, nums2):
            res = []
            for _ in range(len(nums1)+len(nums2)):
                if nums1 > nums2:
                    res.append(nums1[0])
                    nums1 = nums1[1:]
                else:
                    res.append(nums2[0])
                    nums2 = nums2[1:]
            
            return res
        
        
        # iterate over to select i digits from nums1 and k-i digits from nums2,
        # find the max result.
        return max(merge(prepare(nums1, i), prepare(nums2, k-i)) for i in range(k+1) if i<=len(nums1) and k-i <=len(nums2))


class Solution2:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def prepare(nums, k):
            drop = len(nums)-k
            q= []
            for x in nums:
                # mono queue keep it decreasing
                while drop and q and q[-1] < x:
                    q.pop()
                    drop -= 1
                q.append(x)
            
            return q[:k]
        
        def merge(nums1, nums2):
            res = []
            i, j = 0, 0
            while i < len(nums1) and j < len(nums2):
                if greater(nums1, i, nums2, j):
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1
            
            if i < len(nums1):
                res += nums1[i:]
            if j < len(nums2):
                res += nums2[j:]
            
            return res
        
        # check if num1 lexicographically larger than num2
        def greater(nums1, i, nums2, j):
            while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
                i += 1
                j += 1
            
            return j == len(nums2) or (i < len(nums1) and nums1[i] > nums2[j])
        
        
        # iterate over to select i digits from nums1 and k-i digits from nums2,
        # find the max result.
        return max(merge(prepare(nums1, i), prepare(nums2, k-i)) for i in range(k+1) if i<=len(nums1) and k-i <=len(nums2))

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.maxNumber
            self.assertEqual(func([3, 4, 6, 5],[9, 1, 2, 5, 8, 3],5), [9, 8, 6, 5, 3])
            self.assertEqual(func([6, 7],[6, 0, 4],5), [6, 7, 6, 0, 4])
            self.assertEqual(func([3, 9],[8, 9],3), [9, 8, 9])
            self.assertEqual(func([2,5,6,4,4,0],[7,3,8,0,6,5,7,6,2],15), [7,3,8,2,5,6,4,4,0,6,5,7,6,2,0])



if __name__ == '__main__':
    unittest.main()
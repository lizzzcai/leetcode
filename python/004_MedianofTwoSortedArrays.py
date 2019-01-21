"""
18/12/2018

Tag: Array, Recursive, Binary Search

4. Median of Two Sorted Arrays - Hard


There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""

class Solution_0:
    """
    based solution, merge then find the mid value

    Time complexity: O(m+n).

    Space complexity: O(m+n).

    """
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1),  len(nums2)

        if m == 0 and n == 0:
            raise ValueError("lists are both empty.")
        nums = self.merge(nums1, nums2)
        return (nums[(m + n - 1) // 2] + nums[(m + n) // 2]) / 2.0

    def merge(self, nums1, nums2):
        m, n = len(nums1),  len(nums2)
        i, j = 0, 0
        res = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        if i == m:
            res += nums2[j:]
            #while j < m:
            #    res.append(nums2[j])
            #    j += 1
        if j == n:
            res += nums1[i:]
            #while i < n:
            #    res.append(nums1[i])
            #    i += 1
        return res



# Recursive Approach
class Solution:
    """
    Time complexity: O(log(min(m,n))).
    At first, the searching range is [0, m]. And the length of this searching range will be reduced by half after each loop. 
    So, we only need log(m) loops. Since we do constant operations in each loop, so the time complexity is O(log(m)).
    Since m <= n, so the time complexity is O(log(min(m,n))).
    Space complexity: O(1).
    We only need constant memory to store 99 local variables, so the space complexity is O(1).
    """
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        m, n = len(A), len(B)
        # to ensure m <= n
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError("lists are both empty.")
        
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < imax and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > imin and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                
                if i == 0:
                    max_of_left = B[j-1]
                elif j == 0:
                    max_of_left = A[i-1]
                else:
                    max_of_left = max(A[i-1], B[j-1])
                
                if (m + n) % 2 == 1:
                    return max_of_left
                
                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])
                
                return (max_of_left + min_of_right) / 2.0
        


# Unit Test
import unittest
class findMedianSortedArraysCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_findMedianSortedArrays(self):


        # method 0, based method, merge and find median
        print("based method, merge and find median")
        func = Solution_0().findMedianSortedArrays
        self.assertEqual(func([1,3], [2]), 2)
        self.assertEqual(func([1,2], [3,4]), 2.5)
        self.assertEqual(func([1,2,3,4], []), 2.5)
        self.assertRaises(ValueError, func, [],[])


        # Recursive method
        print("Recursive method")

        func = Solution().findMedianSortedArrays
        self.assertEqual(func([1,3], [2]), 2)
        self.assertEqual(func([1,2], [3,4]), 2.5)
        self.assertEqual(func([1,2,3,4], []), 2.5)
        self.assertRaises(ValueError, func, [],[])

if __name__ == '__main__':
    unittest.main()

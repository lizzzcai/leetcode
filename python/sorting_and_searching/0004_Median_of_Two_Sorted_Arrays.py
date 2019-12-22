"""
18/12/2018
23/12/2019 updated


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
class Solution_1:
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
        
# new binary search solution
class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        '''
        Time complexity: O(log(min(m,n))).
        Space: O(1)
        
        even case
        
              0,1,2,3,4         0,1,2,3,4
                    |               |
        num1 [1,3,4,8,9],  num2[2,5,6,7,10]
        
                 0,1,2,3,4,5,6,7,8,9
                          |
        merged: [1,2,3,4,5,6,7,8,9,10]
        
        mean: (5+6)/2.0 = 5.5
        mean = (max(num1[partition1-1], num2[partition2-1]) + min(num1[partition1], num2[partition2])) / 2.0
        conditions:
        partition1 + partition2 = len(merged) // 2
        num1[parition1-1] <= num2[partition2]
        num2[parition2-1] <= num1[partition1]
        if know parittion1, can find partition2
        
        if parition1 = 2, then pratition2 = 3
        num1[partition1-1] = 3 <  num2[partition2] = 7, condition met.
        num1[partition1] = 4 < num2[paritition2-1] = 6, condition not met.
        
        so need to increase the parition1, at the same time parition2 decrease.
        
        
        odd case:
              0,1,2,3,4         0,1,2,3
                    |             |
        num1 [1,3,4,8,9],  num2[2,5,6,7]
        
                 0,1,2,3,4,5,6,7,8,9
                         |
        merged: [1,2,3,4,5,6,7,8,9]
        same conditions
        mean = 5, mean is min(num1[partition1], num2[partition2])
        
        if parition-1 == 0:

              0,1,2,3,4,5       0,1,2,3
                        |       |
        num1 [1,2,3,4,5],  num2[6,7,8,9,10]
        
                 0,1,2,3,4,5,6,7,8,9
                          |
        merged: [1,2,3,4,5,6,7,8,9,10]
        
        num1[partition1] = int.max
        num2[partition2-1] = int.min
        
        '''
        
        n, m = len(nums1), len(nums2)
        if n==0 and m==0:
            raise ValueError("lists are both empty.")
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        
        # let's binary search in nums1
        # there is a case a parition at n, all the num in nums1 are in the left side of merge. so right is n - 1
        left, right = 0, n
        while left <= right:
            # mid:
            p1 = left - (left - right) // 2
            p2 = (n + m) // 2 - p1
            nums1_left = nums1[p1-1] if p1 > 0 else -float("inf")
            nums1_right = nums1[p1] if p1 < n else float('inf')
            nums2_left = nums2[p2-1] if p2 > 0 else -float("inf")
            nums2_right = nums2[p2] if p2 < m else float('inf')

            if nums1_left > nums2_right:
                right = p1 - 1
            elif nums1_right < nums2_left:
                left = p1 + 1
            else:
                if (n + m) % 2 == 0: # if even
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
                else: # odd
                    return min(nums1_right, nums2_right)
            


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
        self.assertEqual(func([1,3,4,8,9], [2,5,6,7,10]), 5.5)
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

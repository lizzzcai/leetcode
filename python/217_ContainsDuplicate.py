'''
04/02/2019

217. Contains Duplicate - Easy

Tag: Array, HashTable

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

# Solution
class Solution:
    '''
    Approach #3 (Hash Table) [Accepted]
    Intuition

    Utilize a dynamic data structure that supports fast search and insert operations.

    Algorithm

    From Approach #1 we know that search operations is O(n) in an unsorted array and we did so repeatedly. Utilizing a data structure with faster search time will speed up the entire algorithm.

    There are many data structures commonly used as dynamic sets such as Binary Search Tree and Hash Table. 
    The operations we need to support here are search() and insert(). For a self-balancing Binary Search Tree (TreeSet or TreeMap in Java), search() and insert() are both O(\log n)O(logn) time. 
    For a Hash Table (HashSet or HashMap in Java), search() and insert() are both O(1)O(1) on average. Therefore, by using hash table, we can achieve linear time complexity for finding the duplicate in an unsorted array.

    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        Htable = set()
        for i in range(len(nums)):
            if nums[i] in Htable:
                return True
            else:
                Htable.add(nums[i])
        return False
            

class Solution2:
    """
    Approach #2 (Sorting) [Accepted]
    Intuition

    If there are any duplicate integers, they will be consecutive after sorting.

    Algorithm

    This approach employs sorting algorithm. Since comparison sorting algorithm like heapsort is known to provide O(n \log n)O(nlogn) worst-case performance, sorting is often a good preprocessing step.
    After sorting, we can sweep the sorted array to find if there are any two consecutive duplicate elements.
    
    Time complexity : O(nlogn)
    Space complexity : O(1) if heapsort
    """

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
            

# Unit Test
import unittest
class containsDuplicateCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_containsDuplicate(self):
        func = Solution().containsDuplicate
        self.assertEqual(func([1,2,3,1]), True)

if __name__ == '__main__':
    unittest.main()
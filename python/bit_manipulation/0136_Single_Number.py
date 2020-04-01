'''
04/02/2019
01/04/2020

136. Single Number - Easy

Tag: Array, HashTable, Bit Manipulation

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

# Solution
class Solution1:
    '''
    Approach 4: Bit Manipulation
    Time complexity : O(n). We only iterate through nums, so the time complexity is the number of elements in nums.

    Space complexity : O(1).
    '''
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        '''        
        Concept
        if we take XOR of zero and some bit, it will return that bit
        a ^ 0 = a
        if we take XOR of two same bits, it will return 0
        a ^ a = 0
        
        so:
        a ^ b ^ a = (a^a)^b = 0^b = b
        
        '''

        for num in nums:
            res ^= num
        return res


class Solution2: 
    '''
    Approach 2: Hash Table
    Algorithm

    We use hash table to avoid the O(n) time required for searching the elements.

    Iterate through all elements in nums
    Try if hash_table has the key for pop
    If not, set up key/value pair
    In the end, there is only one element in hash_table, so use popitem to get it


    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashTable = set()
        for num in nums:
            if num in hashTable:
                hashTable.remove(num)
            else:
                hashTable.add(num)
        return hashTable.pop()



# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.singleNumber
            self.assertEqual(func([4,1,2,1,2]), 4)
            self.assertEqual(func([2,1,2]), 1)

if __name__ == '__main__':
    unittest.main()
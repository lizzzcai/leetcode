'''
09/02/2019

38. Count and Say - Easy

Tag: String


The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"

'''

# Solution
class Solution:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        hmap = {} # store the difference between target and selected num.
        res = [] # res list
        for i in range(n):
            # check if the num in the hashmap.
            if nums[i] in hmap:
                # if in the map, means previous there is a value which
                # meets the requirement (previous + current = target)
                
                res.append(hmap[nums[i]]) # the previous value should be placed at the first
                res.append(i)
                return res
            else:
                # if not in the map, add the future value which meet 
                # the requirement with this current value in the map
                # for retrieve in the next.
                # {(target - current) : index of current num}
                hmap[target - nums[i]] = i

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().twoSum
        self.assertEqual(func([2, 7, 11, 15], 9), [0, 1])

if __name__ == '__main__':
    unittest.main()
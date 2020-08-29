'''
20/08/2020

470. Implement Rand10() Using Rand7() - Medium

Tag: Random, Rejection Sampling

Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().

 

Example 1:

Input: 1
Output: [7]
Example 2:

Input: 2
Output: [8,4]
Example 3:

Input: 3
Output: [8,1,10]
 

Note:

rand7 is predefined.
Each testcase has one argument: n, the number of times that rand10 is called.
 

Follow up:

What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?

'''

from typing import List
import random
# Solution
class Solution1:
    '''
    Rejection Sampling
    Time complexity : O(1)
    Space complexity : O(1)
    '''
    def rand10(self):
        """
        :rtype: int
        """

        def rand7():
            return random.randint(1,7)

        index = 41
        
        while index > 40:
            row = rand7()
            col = rand7()
            index = (row-1)*7+col
        
        return 1+(index-1)%10

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.rand10
            self.assertTrue(1<=func()<=10)

if __name__ == '__main__':
    unittest.main()
'''
20/09/2020

1291. Sequential Digits - Medium

Tag: Backtracking

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9

'''

from typing import List
# Solution
class Solution1:
    '''

    '''
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def gen(digit):
            num = nxt = digit
            while num <= high and nxt < 10:
                if num >= low:
                    yield num
                nxt += 1
                num = num*10 + nxt
                
        return sorted([x for i in range(1,10) for x in gen(i)])


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.sequentialDigits
            self.assertEqual(func(100,300), [123, 234])
            self.assertEqual(func(1000,13000), [1234,2345,3456,4567,5678,6789,12345])


if __name__ == '__main__':
    unittest.main()
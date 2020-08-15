'''
14/08/2020

1286. Iterator for Combination - Medium

Tag: Backtracking, Design

Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
 

Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.

'''

from typing import List
# Solution
class CombinationIterator1:
    '''
    Backtracking with Generator
    https://leetcode.com/problems/iterator-for-combination/discuss/451260/python-using-generator
    '''
    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.len = combinationLength
        self.gen = self.generator()
        self.curr = self.gen
        self.last = self.chars[-self.len:]

    def generator(self):
        
        def backtrack(start, path):
            if len(path) == self.len:
                yield ''.join(path)
                return
                
            for i in range(start, len(self.chars)):
                yield from backtrack(i+1, path + [self.chars[i]])

        return backtrack(0, [])
        
        
    def next(self) -> str:
        self.curr = next(self.gen)
        return self.curr
        

    def hasNext(self) -> bool:
        return self.curr != self.last
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()



# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [CombinationIterator1]:
            func = Sol("abc", 2)
            self.assertEqual(func.next(), "ab")
            self.assertEqual(func.hasNext(), True)
            self.assertEqual(func.next(), "ac")
            self.assertEqual(func.hasNext(), True)
            self.assertEqual(func.next(), "bc")
            self.assertEqual(func.hasNext(), False)


if __name__ == '__main__':
    unittest.main()
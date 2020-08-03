'''
01/07/2020

705. Design HashSet - Easy

Tag: Design, Hash Table

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.

'''

from typing import List
# Solution
class MyHashSet1:

    def __init__(self):
        """
        Initialize your data structure here.
        https://leetcode.com/problems/design-hashset/discuss/152654/Python-hash-set-with-trivial-hash-function
        """
        
        self.data = [[]]*1000
        
    def hash_func(self, key: int) -> int:
        return key % 1000
    
    def find(self, key: int) -> (int, int):
        idx = self.hash_func(key)
        for i, x in enumerate(self.data[idx]):
            if x == key:
                return (idx, i)
        
        return (idx, -1)
        

    def add(self, key: int) -> None:
        idx, pos = self.find(key)
        if pos == -1:
            self.data[idx].append(key)

    def remove(self, key: int) -> None:
        idx, pos = self.find(key)
        if pos != -1:
            self.data[idx].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx, pos = self.find(key)
        return pos >= 0


class MyHashSet2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 1000
        self.data = [[]] * self.cap
        self.lf = 0.75
        self.n = 0
        
    def hash_func(self, key: int) -> int:
        return key % self.cap
    
    def find(self, key: int) -> (int, int):
        idx = self.hash_func(key)
        for i, x in enumerate(self.data[idx]):
            if x == key:
                return (idx, i)
        
        return (idx, -1)
    
    
    def rehash(self):
        old = self.data
        self.n = 0
        self.cap = self.cap * 2
        self.data = [[]] * self.cap
        
        for slot in old:
            if len(slot) > 0:
                for x in slot:
                    self.add(x)
    
    def add(self, key: int) -> None:
        if self.n > self.cap * self.lf:
            # extend the arr and rehash
            self.rehash()
            
        idx, pos = self.find(key)
        if pos == -1:
            self.data[idx].append(key)
            self.n += 1

    def remove(self, key: int) -> None:
        idx, pos = self.find(key)
        if pos != -1:
            self.data[idx].remove(key)
            self.n -= 1

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx, pos = self.find(key)
        return pos >= 0
        



# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [MyHashSet1(), MyHashSet2()]:
            obj = Sol
            obj.add(1)
            obj.add(2)
            self.assertEqual(obj.contains(1), True)
            self.assertEqual(obj.contains(3), False)
            obj.add(2)
            self.assertEqual(obj.contains(2), True)
            obj.remove(2)
            self.assertEqual(obj.contains(2), False)


if __name__ == '__main__':
    unittest.main()
'''
04/08/2020

706. Design HashMap - Easy

Tag: Design, Hash Table

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.

'''

from typing import List
# Solution
class MyHashMap1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 1000
        self.data = [[]] * self.cap
        self.lf = 0.75
        self.n = 0
    
    def hash(self, key):
        return key % self.cap
    
    def find(self, key):
        idx = self.hash(key)
        for i, x in enumerate(self.data[idx]):
            if x[0] == key:
                return (idx, i)
        
        return (idx, -1)
    
    def rehash(self):
        old = self.data
        self.n = 0
        self.cap *= 2
        self.data = [[]]*self.cap
        
        for slot in old:
            if len(slot) > 0:
                for k, v in slot:
                    self.put(k, v)
    
    
    
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        
        if self.n >= self.cap * self.lf:
            self.rehash()
        
        idx, pos = self.find(key)
        if pos == -1:
            self.data[idx].append((key, value))
            self.n += 1
        else:
            if self.data[idx][pos][1] != value:
                self.data[idx][pos] = (key, value)
        
        
        
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx, pos = self.find(key)
        if pos == -1:
            return -1
        
        return self.data[idx][pos][1]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx, pos = self.find(key)
        if pos == -1:
            return
        
        self.data[idx].pop(pos)
        self.n -= 1



class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None


class MyHashMap2:

    def __init__(self):
        """
        Initialize your data structure here.
        https://leetcode.com/problems/design-hashmap/discuss/185347/Hash-with-Chaining-Python
        """
        self.cap = 1000
        self.data = [None] * self.cap
        self.lf = 0.75
        self.n = 0
    
    def hash(self, key):
        return key % self.cap
    
    def find(self, key):
        idx = self.hash(key)
        if self.data[idx] != None:
            node = self.data[idx]
            # get the node before the target
            while node.next and node.next.pair[0] != key:
                node = node.next

        else:
            node = ListNode(None, None)
            self.data[idx] = node
        
        return (idx, node)
    
    
    def rehash(self):
        old = self.data
        self.n = 0
        self.cap *= 2
        self.data = [None] * self.cap
        
        for slot in old:
            if slot != None:
                node = slot.next
                while node:
                    k, v = node.pair
                    self.put(k, v)
                    node = node.next
    
    
    
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        
        if self.n >= self.cap * self.lf:
            self.rehash()
        
        idx, node = self.find(key)
        if node.next == None:
            node.next = ListNode(key, value)
            self.n += 1
        else:
            if node.next.pair[1] != value:
                node.next.pair = (key, value)
        
        
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx, node = self.find(key)
        if node.next == None:
            return -1
        
        return node.next.pair[1]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx, node = self.find(key)
        if node.next == None:
            return None
        
        target = node.next
        after = target.next
        target.next = None
        node.next = after
        self.n -= 1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [MyHashMap1(), MyHashMap2()]:
            obj = Sol
            obj.put(1, 1)
            obj.put(2, 2)
            self.assertEqual(obj.get(1), 1)
            self.assertEqual(obj.get(3), -1)
            obj.put(2,1)
            self.assertEqual(obj.get(2), 1)
            obj.remove(2)
            self.assertEqual(obj.get(2), -1)


if __name__ == '__main__':
    unittest.main()
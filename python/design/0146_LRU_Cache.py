'''
25/04/2020

146. LRU Cache - Medium

Tag: Design

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
 

'''

from typing import List
import collections

class Node:
    def __init__(self,k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

# Solution
    '''
    Time complexity : O(1)
    Space complexity : O(n)
    '''
class LRUCache_1:

    def __init__(self, capacity: int):
        self.dict = {}
        self.cap = capacity
        self.count = 0
        self.head = Node(0,0)
        self.tail = Node(0,0)
        # connect linkedlist
        self.head.next = self.tail
        self.tail.prev = self.head
        
        

    def get(self, key: int) -> int:
        if key in self.dict:
            n = self.dict[key]
            # remove the node
            self.__remove(n)
            # add back the node as latest
            self.__add(n)
            return n.val
            
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            # remove the old key
            self.__remove(self.dict[key])
            self.count -= 1
            
        # add the node
        n = Node(key, value)
        self.__add(n)
        self.dict[key] = n
        self.count += 1
        
        if self.count > self.cap:
            # remove the least from linked list
            least = self.head.next
            self.__remove(least)
            # remove the least from dict
            self.dict.pop(least.key)
            self.count -= 1
        
        
    def __add(self, n):
        prev = self.tail.prev
        prev.next = n
        n.prev = prev
        n.next = self.tail
        self.tail.prev = n
    
    def __remove(self, n):
        prev = n.prev
        nxt = n.next
        prev.next = nxt
        nxt.prev = prev

class LRUCache_2:
    '''
    using ordered dict
    '''
    def __init__(self, capacity: int):
        self.dict = collections.OrderedDict()
        self.cap = capacity
        self.count = 0
        

    def get(self, key: int) -> int:
        if key in self.dict:
            self.dict.move_to_end(key)
            return self.dict[key]
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
            self.count -= 1
        
        self.dict[key] = value
        self.count += 1
        if self.count > self.cap:
            self.dict.popitem(last=False)
            self.count -= 1


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [LRUCache_1(2), LRUCache_2(2)]:
            obj = Sol
            obj.put(1,1)
            obj.put(2,2)
            self.assertEqual(obj.get(1), 1)
            obj.put(3,3)
            self.assertEqual(obj.get(2), -1)
            obj.put(4,4)
            self.assertEqual(obj.get(1), -1)
            self.assertEqual(obj.get(3), 3)
            self.assertEqual(obj.get(4), 4)

if __name__ == '__main__':
    unittest.main()
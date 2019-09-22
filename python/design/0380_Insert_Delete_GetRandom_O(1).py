"""
22/09/2019
380. Insert Delete GetRandom O(1) - Medium
Tag: dict

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.idx = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.idx:
            return False
        else:
            # append value into data 
            self.data.append(val)
            
            # record the idx of the value in data
            self.idx[val] = len(self.data) - 1
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.idx:
            # swap the target value and the last value in the data set
            last_val, val_idx = self.data[-1], self.idx[val]
            self.data[val_idx], self.idx[last_val] = last_val, val_idx
            self.data.pop()
            self.idx.pop(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.data:
            return self.data[random.randrange(len(self.data))]
        else:
            return None

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.insert(1))
print(obj.insert(2))
print(obj.remove(2))
print(obj.remove(2))
print(obj.remove(1))
print(obj.remove(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.remove(1))
print(obj.getRandom())

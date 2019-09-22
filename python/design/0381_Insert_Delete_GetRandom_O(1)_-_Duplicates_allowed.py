"""
22/09/2019
381. Insert Delete GetRandom O(1) - Duplicates allowed - Hard
Tag: dict, set


Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.
Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
Accepted
"""


import random
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.index = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        # insert value into data
        self.data.append(val)
        # insert the index of the value into index dict
        # use set for O(1) search
        self.index.setdefault(val, set()).add(len(self.data)-1)
        # if the index of the given value, has only one value, means the collection did not alreawdy contain the element.
        return len(self.index[val]) == 1
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        # if the collection include the value (has index), process to remove it and return True, else return False
        if self.index.setdefault(val, set()):
            # get the last value of the data, and the index of the value to be removed
            last_val, index_val = self.data[-1], self.index[val].pop()
            # swap the value to the last value, update the index of the last value
            self.data[-1], self.data[index_val] = val, last_val
            # update the indx of the last_val
            # add index first then remove it, to avoid the case that remove value is at the end of the data.
            self.index[last_val].add(index_val)
            self.index[last_val].remove(len(self.data)-1)
            # remove the val from the end of data
            self.data.pop()
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        if self.data:
            return self.data[random.randrange(len(self.data))]
        else:
            return None

# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
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
'''
06/05/2020

1146. Snapshot Array - Medium

Tag: Array

Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
 

Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 

Constraints:

1 <= length <= 50000
At most 50000 calls will be made to set, snap, and get.
0 <= index < length
0 <= snap_id < (the total number of times we call snap())
0 <= val <= 10^9

'''

from typing import List
# Solution
class SnapshotArray:
    '''
    Time O(logS)
    Space O(S)
    '''
    def __init__(self, length: int):
        self.data = [[[-1, 0]] for _ in range(length)] # (id, val)
        self.snap_id = 0
        
    def set(self, index: int, val: int) -> None:
        self.data[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        idx = self.__binarysearch(self.data[index], snap_id)
        return self.data[index][idx][1]
        

    def __binarysearch(self, arr, target):
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l+r) // 2
            if arr[mid][0] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return r
    

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [SnapshotArray]:
            func = Sol(3)
            func.set(0, 5)
            self.assertEqual(func.snap(), 0)
            func.set(0,6)
            self.assertEqual(func.get(0, 0), 5)
if __name__ == '__main__':
    unittest.main()
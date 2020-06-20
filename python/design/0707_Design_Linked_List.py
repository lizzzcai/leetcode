'''
17/06/2020

707. Design Linked List - Medium

Tag: Linked List, Design 

Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
 

Example:

Input: 
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]
Output:  
[null,null,null,null,2,null,3]

Explanation:
MyLinkedList linkedList = new MyLinkedList(); // Initialize empty LinkedList
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
 

Constraints:

0 <= index,val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail,  addAtIndex and deleteAtIndex.
'''

from typing import List
# Solution
class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.n = 0
        self._head = Node(None)
        self._tail = Node(None)
        self._head.next = self._tail
        self._tail.prev = self._head
        
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if 0<= index < self.n:
            dummy = self._head.next
            while index > 0:
                dummy = dummy.next
                index -= 1
            return dummy.val
        
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        # insert the new node between head and first node
        old_first = self._head.next
        new_first = Node(val)
        new_first.next = old_first
        new_first.prev = self._head
        old_first.prev = new_first
        self._head.next = new_first
        self.n += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        # insert the new node between last node and tail
        old_last = self._tail.prev
        new_last = Node(val)
        old_last.next = new_last
        new_last.prev = old_last
        new_last.next = self._tail
        self._tail.prev = new_last
        self.n += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
        elif index == self.n:
            self.addAtTail(val)
        elif 0 < index < self.n:
            # get the idx-th node
            idx_node = self._head.next
            while index > 0:
                idx_node = idx_node.next
                index -= 1
            node_before = idx_node.prev
            
            # insert the new node between node_before and idx_node
            new_node = Node(val)
            node_before.next, new_node.prev = new_node, node_before
            new_node.next, idx_node.prev = idx_node, new_node
            self.n += 1
        else:
            return
        
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self.n:
            # get the idx-th node
            idx_node = self._head.next
            while index > 0:
                idx_node = idx_node.next
                index -= 1
            # get the node before and after the index node
            node_before = idx_node.prev
            node_after = idx_node.next
            
            # remove the index_node
            node_before.next, node_after.prev = node_after, node_before
            self.n -= 1

        else:
            return
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)



# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        LinkedList = MyLinkedList()
        LinkedList.addAtHead(1)
        LinkedList.addAtTail(3)
        LinkedList.addAtIndex(1,2)
        self.assertEqual(LinkedList.get(1), 2)
        LinkedList.deleteAtIndex(1)
        self.assertEqual(LinkedList.get(1), 3)



if __name__ == '__main__':
    unittest.main()
"""
25/12/2018

Tag: LinkedList

25. Reverse Nodes in k-Group - Hard

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
-1 is the dummy head
if k = 3

-1->1->2->3->4->5
 |           |
pre         next

-1->3->2->1->4->5
          |  |
         pre next

"""


class Solution1:

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        dummyhead.next = head

        current = dummyhead
        while current is not None:
            # current is the dummyhead of each group
            current = self.reverseK(current, k)
        return dummyhead.next
        
        
    """
    dummyhead -> A -> B -> C -> D -> E, k = 3
    In order to reverse A -> B -> C, you have to:
        B -> A,
        C -> B,
        A -> D,
        dummyhad->C,
        so we have: 
        dummyhead -> C -> B -> A -> D -> E
        return A as the dummyhead of next group (D,E ...)
    """
    def reverseK(self, head, k):
        # head is the dummy head
        current = head
        # check if enough nodes to be reversed
        for _ in range(k):
            if current.next is None:
                return None
            current = current.next
        
        # last node in reversed nodeList
        node = head.next
        # define the prev and curr
        prev = head
        curr = prev.next
        # reverse this group
        for _ in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # connect the last node in the reversed nodeList (first node of this group before reversed) to the first node of next group
        # the last node of the reversed nodelist will be the dummyhead of the nextg group
        node.next = curr
        # connect the dummyhead of this group to the first node of the reversed nodeList
        # (last node of this group before reversed)
        head.next = prev
        return node

# Recursive
class Solution2:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k:
            print(f"count:{count}<{k}, return {head.val}")
            return head
        print("reverse:", head.val, "count:", count)
        new_head, prev = self.reverse(head, count)
        print("new_head:",new_head.val, "prev:", prev.val)
        print("reverseKGroup, new_head:", new_head.val," k:", k)
        print("head:", head.val)
        print("-----")
        head.next = self.reverseKGroup(new_head, k)
        print("*head:", head.val, "->", head.next.val)
        print("*prev:",prev.val)
        return prev
    
    def reverse(self, head, count):
        prev, curr = None, head
        while count > 0:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
            count -= 1
        return (curr, prev)



def create_ListNode(valueList):
    """function to create ListNode from a list of int
    
    Arguments:
        valueList {List} -- a list of int
    
    Returns:
        ListNode -- ListNode represent a non-negative integer
    """

    dummyhead = ListNode(0)
    curr = dummyhead
    for val in valueList:
        if val < 0:
            raise ValueError("value list contains negative integer")
        curr.next = ListNode(val)
        curr = curr.next
    return dummyhead.next

def listNode2List(listNode):
    """function to convert listNode to list for easy compare and display
    
    Arguments:
        listNode {ListNode} -- a ListNode representing a non-negative integer
    
    Returns:
        res {list} -- list of non-negative integer to represent a ListNode
    """
    
    res = []
    curr = listNode
    while curr != None:
        x = curr.val
        res.append(x)
        if curr != None:
            curr = curr.next
    return res

  
        
# Unit Test
import unittest
class ReverseNodesInKGroupCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ReverseNodesInKGroup(self):
        func = Solution1().reverseKGroup
        l1 = create_ListNode([1,2,3,4,5])
        l2 = create_ListNode([2,1,4,3,5])
        print(listNode2List(l1))
        print(listNode2List(l2))
        res = func(l1,2)
        print(listNode2List(res))
        self.assertEqual(listNode2List(res), listNode2List(l2))

        func = Solution2().reverseKGroup
        l1 = create_ListNode([1,2,3,4,5])
        l2 = create_ListNode([2,1,4,3,5])
        print(listNode2List(l1))
        print(listNode2List(l2))
        res = func(l1,2)
        print(listNode2List(res))
        self.assertEqual(listNode2List(res), listNode2List(l2))



if __name__ == '__main__':
    unittest.main()

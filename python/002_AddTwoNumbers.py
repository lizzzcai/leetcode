'''
18/12/2018

Tag: LinkedList

2. Add Two Numbers - Medium


You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    Time complexity : O(max(m,n)). Assume that m and n represents the length of l1 and l2 respectively, the algorithm above iterates at most max(m,n) times.
    Space complexity : O(max(m,n)). The length of the new list is at most max(m,n)+1.
    '''
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Initialize current node to dummy head of the returning list.
        dummyHead = ListNode(0)
        p, q, curr = l1, l2, dummyHead
        carry = 0
        # Loop through lists l1 and l2 until you reach both ends.
        while (p != None or q != None):
            # Set x to node p's value. If p has reached the end of l1, set to 0.
            x = p.val if p != None else 0
            # Set y to node q's value. If q has reached the end of l2, set to 0.
            y = q.val if q != None else 0
            sumVal = carry + x + y
            # update carry = (int)sum/10 
            carry = sumVal // 10
            # Create a new node with the digit value of (sum mod 10) and set it to
            # current node's next, then advance current node to next
            curr.next = ListNode(sumVal % 10) 
            curr = curr.next
            # advance both p and q
            if p != None:
                p = p.next
            if q != None:
                q = q.next
        
        # check if carry = 1, if so append a new node with digit 1 to the returning list
        if (carry > 0):
            curr.next = ListNode(carry)
        # Return dummy head's next node.
        return dummyHead.next


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
class addTwoNumbersCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_addTwoNumbers(self):
        func = Solution().addTwoNumbers
        # test 1
        l1 = create_ListNode([2,4,3])
        l2 = create_ListNode([5,6,4])
        res = func(l1,l2)
        print(listNode2List(res))
        self.assertEqual(listNode2List(res), [7,0,8])

        # test 2
        l1 = create_ListNode([0,1])
        l2 = create_ListNode([0,1,2])
        res = func(l1,l2)
        print(listNode2List(res))
        self.assertEqual(listNode2List(res), [0,2,2])

        # test 3
        l1 = create_ListNode([])
        l2 = create_ListNode([0,1])
        res = func(l1,l2)
        print(listNode2List(res))
        self.assertEqual(listNode2List(res), [0,1])

        # test 4
        l1 = create_ListNode([9,9])
        l2 = create_ListNode([1])
        res = func(l1,l2)
        print(listNode2List(res))
        self.assertEqual(listNode2List(res), [0,0,1])




if __name__ == '__main__':
    unittest.main()
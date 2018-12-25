"""
24/12/2018

Tag: LinkedList

206. Reverse Linked List - Easy

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



# Reversed iteratively
"""
Approach #1 (Iterative) [Accepted]
Assume that we have linked list 1 → 2 → 3 → Ø, we would like to change it to Ø ← 1 ← 2 ← 3.

While you are traversing the list, change the current node's next pointer to point to its previous element. 
Since a node does not have reference to its previous node, you must store its previous element beforehand. 
You also need another pointer to store the next node before changing the reference. Do not forget to return the new head reference at the end!
"""
class Solution1:
    """
    Time complexity : O(n). Assume that n is the list's length, the time complexity is O(n).

    Space complexity : O(1).
    """
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        prev, curr = None, head
        while curr != None: # while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev
            
"""
Approach #2 (Recursive) [Accepted]
The recursive version is slightly trickier and the key is to work backwards. 
Assume that the rest of the list had already been reversed, now how do I reverse the front part? 
Let's assume the list is: n1 → … → nk-1 → nk → nk+1 → … → nm → Ø

Assume from node nk+1 to nm had been reversed and you are at node nk.

n1 → … → nk-1 → nk → nk+1 ← … ← nm

We want nk+1’s next node to point to nk.

So,

nk.next.next = nk;

Be very careful that n1's next must point to Ø. If you forget about this, your linked list has a cycle in it. 
This bug could be caught if you test your code with a linked list of size 2.



Time complexity : O(n). Assume that n is the list's length, the time complexity is O(n).

Space complexity : O(n). The extra space comes from implicit stack space due to recursion. The recursion could go up to nn levels deep.

"""
class Solution2:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # base case
        if head == None or head.next == None:
            print("reach end ",head.val)
            return head
        print("reverse head.next, value:", head.val)
        new_head = self.reverseList(head.next)
        print("process, head: ", head.val)
        print(head.val, " -> ",head.next.val)
        print(head.next.val, " -> ", head.val)
        print(head.val, " -> None")

        head.next.next = head
        head.next = None
        return new_head



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
class ReverseLinkedListCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ReverseLinkedList(self):
        # SOLUTION 1
        func = Solution1().reverseList
        l1 = create_ListNode([0,1,2,3,4,5])
        l2 = create_ListNode([5,4,3,2,1,0])
        print(listNode2List(l1))
        print(listNode2List(l2))
        res = func(l1)
        print(listNode2List(res))
        self.assertEqual(listNode2List(res), listNode2List(l2))

        # SOLUTION 2
        func = Solution2().reverseList
        l1 = create_ListNode([0,1,2,3,4,5])
        l2 = create_ListNode([5,4,3,2,1,0])
        print(listNode2List(l1))
        print(listNode2List(l2))
        res = func(l1)
        print(listNode2List(res))
        self.assertEqual(listNode2List(res), listNode2List(l2))




if __name__ == '__main__':
    unittest.main()

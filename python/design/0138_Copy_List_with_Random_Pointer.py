"""
22/09/2019
138. Copy List with Random Pointer - Medium
Tag: dict, linked list


A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

 

Example 1:



Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

Note:

You must return the copy of the given head as a reference to the cloned list.

"""




# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # dict to store each Node of head,
        # key is the node in the head, value is the new node.
        hmap = {}
        # have two copys of head
        m, n = head, head
        while m:
            # for each node in head, make a copy with value
            hmap[m] = Node(m.val, None, None)
            m = m.next
        
        while n:
            # for each node in head, get the copy node from dict and update the next and random value
            hmap[n].next = hmap.get(n.next)
            hmap[n].random = hmap.get(n.random)
            n = n.next
        
        # return the head node of the copy linked list
        return hmap.get(head)


class Solution1:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # dict to store each Node of head,
        # key is the node in the head, value is the new node.
        hmap = {}
        hmap[None] = None
        # have a of head
        n = head
        
        while n:
            # store the current node n, if not exist, make a copy and assign the value
            hmap.setdefault(n, Node(None, None, None)).val = n.val
            # set the next and random values of the copy node, if not exist, create a new node for them.
            hmap[n].next = hmap.setdefault(n.next, Node(None, None, None))
            hmap[n].random = hmap.setdefault(n.random, Node(None, None, None))
            n = n.next
        
        return hmap[head]
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list_to_linkedlist(val_list):
    head = node = ListNode(None)
    for val in val_list:
        node.next = ListNode(val)
        node = node.next
    return head.next

def linkedlist_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res
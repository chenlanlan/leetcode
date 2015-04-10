#!/user/bin/python

def mergeTwoLists(self, l1, l2):
    node = root = ListNode(0)
    node1 = l1
    node2 = l2
    while node1 and node2:
        if node1.val < node2.val:
            node.next = node1
            node1 = node1.next
        else:
            node.next = node2
            node2 = node2.next
        node = node.next
    if node1:
        node.next = node1
    else:
        node.next = node2
    return root.next

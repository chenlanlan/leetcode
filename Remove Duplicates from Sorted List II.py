#!/user/bin/python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        node = ListNode(0)
        node.next = head
        p = node
        temp = node.next
        while p.next:
            while temp.next != None and p.next.val == temp.next.val:
                temp = temp.next
            if temp == p.next:
                p = p.next
                temp = p.next
            else:
                p.next = temp.next
        return node.next
                

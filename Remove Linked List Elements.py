#!/usr/bin/python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        node = ListNode(0)
        node.next = head
        p = node
        q = head
        while p.next != None:
            if q.val == val:
                p.next = q.next
            else:
                p = p.next
            q = q.next
        return node.next

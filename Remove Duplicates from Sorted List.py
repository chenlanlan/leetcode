#!/usr/bin/python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        node = head
        while node:
            while node.next != None and node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return head
                

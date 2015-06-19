#!/usr/bin/python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return
        nodes = []
        p = head
        while p:
            nodes.append(p)
            p = p.next
        left = 0
        right = len(nodes) - 1
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            nodes[right].next = nodes[left]
            right -= 1
        nodes[left].next = None


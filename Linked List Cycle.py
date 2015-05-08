#!/usr/bin/python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None:
            return False
        fast = ListNode(0)
        slow = ListNode(0)
        fast = head
        fast = fast.next
        slow = head
        while fast != None and fast.next != None:
            if fast == slow:
                return True   
            fast = fast.next.next
            slow = slow.next
        return False
            

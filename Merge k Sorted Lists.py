#!/usr/bin/python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeLists(self, A, B):
        node = root = ListNode(0)
        while A or B:
            if not B or A and A.val < B.val:
                node.next = ListNode(A.val)
                A = A.next
            else:
                node.next = ListNode(B.val)
                B = B.next
            node = node.next
        return root.next
    
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[: mid])
        right = self.mergeKLists(lists[mid :])
        return self.mergeLists(left, right)
                

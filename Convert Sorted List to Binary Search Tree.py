#!/usr/bin/python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        count = 0
        p = head
        while p:
            p = p.next
            count += 1
        return self.convert(head, 0, count - 1)

    def convert(self, head, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        p  = head
        for i in range(left, mid):
            p = p.next
        left = self.convert(head, left, mid - 1)
        right = self.convert(p.next, mid + 1, right)
        root = TreeNode(p.val)
        root.left = left
        root.right = right
        return root

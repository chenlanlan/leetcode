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
        p = head
        count = 0
        while p != None:
            count += 1
            p = p.next
        def Tree(node, left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            p = node
            for i in range(left, mid):
                p = p.next
            leftNode = Tree(node, left, mid - 1)
            rightNode = Tree(p.next, mid + 1, right)
            treeNode = TreeNode(p.val)
            treeNode.left = leftNode
            treeNode.right = rightNode
            return treeNode
        return Tree(head, 0, count - 1)

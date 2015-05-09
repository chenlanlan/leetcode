#!/usr/bin/python

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

'''
另设指针p, 对树的每一层遍历，当p为None时， 该层TreeNode都已经连上了。
'''

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None or root.left == None:
            return
        p = root
        while p != None:
            p.left.next = p.right
            if p.next:
                p.right.next = p.next.left
            p = p.next
        self.connect(root.left)
        return

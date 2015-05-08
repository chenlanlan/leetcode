#!/usr/bin/python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def determin(self, p, q):
            if p == None and q == None:
                return True
            if p and q and p.val == q.val:
                return self.determin(p.left, q.right) and self.determin(p.right, q.left)
            return False
    def isSymmetric(self, root):
        if root == None:
            return True
        if root:
            return self.determin(root.left, root.right)        

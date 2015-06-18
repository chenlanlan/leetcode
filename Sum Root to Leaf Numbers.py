#!/usr/bin/pythons

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        self.sum = 0

    def sumNumbers(self, root):
        if not root:
            return 0
        self.subSum(root, 0)
        return self.sum

    def subSum(self, root, val):
        if not root.left and not root.right:
            self.sum += val * 10 + root.val
        if root.left:
            self.subSum(root.left, val * 10 + root.val)
        if root.right:
            self.subSum(root.right, val * 10 + root.val)
        

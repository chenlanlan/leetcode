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
    def treeDepth(self, root):
        if root == None:
            return 0
        return max(self.treeDepth(root.left), self.treeDepth(root.right)) + 1
        
    def isBalanced(self, root):
        if root == None: 
            return True
        if abs(self.treeDepth(root.left) - self.treeDepth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

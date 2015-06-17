#!/usr/bin/python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root ==  None:
            return False
        temp = 0
        return self.pathSum(root, sum, temp)
    
    def pathSum(self, root, sum, temp):
        if not root:
            return False
        temp += root.val
        if not root.right and not root.left:
            if temp == sum:
                return True
            else:
                return False
        return self.pathSum(root.left, sum, temp) or self.pathSum(root.right, sum, temp)

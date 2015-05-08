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
        def PathSum(root, sum, val):
            if root == None:
                return False
            val += root.val
            if root.left == None and root.right == None:
                if sum == val:
                    return True
                else:
                    return False
            return PathSum(root.left, sum, val) or PathSum(root.right, sum, val)
        return PathSum(root, sum, 0)

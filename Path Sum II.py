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
    # @return a list of lists of integers
    def __init__(self):
        self.res = []

    def pathSum(self, root, sum):
        temp = []
        self.path(root, sum, temp)
        return self.res

    def path(self, root, sum, temp):
        if not root:
            return
        if not root.left and not root.right and sum == root.val:
            temp.append(root.val)
            self.res.append(temp[:])
            return
        sum -= root.val
        temp.append(root.val)
        self.path(root.left, sum, temp[:])
        self.path(root.right, sum, temp[:])


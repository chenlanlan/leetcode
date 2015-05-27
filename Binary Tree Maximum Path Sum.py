#!/usr/bin/python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def __init__(self):
        self.ans = INT_MIN

    def PathSum(self, root):
        if root == None:
            return 0
        sum = root.val
        leftSum = PathSum(root.left)
        rightSum = PathSum(root.right)
        if leftSum > 0:
            sum += leftSum
        if rightSum > 0:
            sum += rightSum
        ans = max(ans, sum)
        sum = max(leftSum, rightSum)
        if sum > 0:
            return root.val + sum
        else:
            return root.val
        
    def maxPathSum(self, root):
        self.PathSum(root)
        return self.ans



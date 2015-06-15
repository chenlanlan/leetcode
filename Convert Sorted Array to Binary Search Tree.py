#!/usr/bin/python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def tree(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        left = self.tree(nums, left, mid - 1)
        right = self.tree(nums, mid + 1, right)
        root = TreeNode(nums[mid])
        root.left = left
        root.right = right
        return root
    
    def sortedArrayToBST(self, nums):
        return self.tree(nums, 0, len(nums) - 1)

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
    def sortedArrayToBST(self, nums):
        n = len(nums)
        def Tree(node, left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            leftNode = Tree(nums, left, mid - 1)
            rightNode = Tree(nums, mid + 1, right)
            treeNode = TreeNode(nums[mid])
            treeNode.left = leftNode
            treeNode.right = rightNode
            return treeNode
        return Tree(nums, 0, n - 1)

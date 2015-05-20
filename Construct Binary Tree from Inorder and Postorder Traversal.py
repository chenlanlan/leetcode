#!/usr/bin/python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def build(self, inorder, isi, iei, postorder, psi, pei):
        if iei < isi or iei - isi != pei - psi:
            return None
        root = TreeNode(postorder[pei])
        riii = -1
        i = isi
        while i <= iei:
            if inorder[i] == root.val:
                riii = i
                break
            i += 1
        if riii == -1:
            return root
        nodeLen = riii - isi
        root.left = self.build(inorder, isi, riii - 1, postorder, psi, psi + nodeLen - 1)
        root.right = self.build(inorder, riii + 1, iei, postorder, psi + nodeLen, pei - 1)
        return root
    
    def buildTree(self, inorder, postorder):
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        else:
            return self.build(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)


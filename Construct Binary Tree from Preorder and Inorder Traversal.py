#!/usr/bin/python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def build(self, preorder, psi, pei, inorder, isi, iei):
        if iei < isi or iei - isi != pei - psi:
            return None
        root = TreeNode(preorder[psi])
        riii = -1
        i = 0
        while i <= iei:
            if inorder[i] == root.val:
                riii = i
                break
            i += 1
        if riii == -1:
            return root
        nodeLen = riii - isi       
        root.left = self.build(preorder, psi + 1, psi + nodeLen, inorder, isi, riii - 1)
        root.right = self.build(preorder, psi + nodeLen + 1, pei, inorder, riii + 1, iei)
        return root

    def buildTree(self, preorder, inorder):
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        else:
            return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
        
        

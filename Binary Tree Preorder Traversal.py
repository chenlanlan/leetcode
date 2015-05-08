#!/usr/bin/python

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def __init__(self):
        self.res = []
    def preorderTraversal(self, root):
        def traversal(root):
            if root == None:
                return
            self.res.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        traversal(root)
        return self.res

#!/usr/bin/python

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root):
        def traversal(root):
            if root == None:
                return
            self.inorderTraversal(root.left)
            self.res.append(root.val)
            self.inorderTraversal(root.right)
        traversal(root)
        return self.res

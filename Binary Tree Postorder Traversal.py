#!/usr/bin/python

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def __init__(self):
        self.res = []
    def postorderTraversal(self, root):
        def traversal(root):
            if root == None:
                return
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.res.append(root.val)
        traversal(root)
        return self.res

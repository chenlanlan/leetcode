#!/usr/bin/python

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def __init__(self):
        self.res = []
    
    def traversal(self, root):
        if root == None:
            return self.res
        self.traversal(root.left)
        self.traversal(root.right)
        self.res.append(root.val)
    
    def postorderTraversal(self, root):
        self.traversal(root)
        
        return self.res

#!/user/bin/python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        self.sum = 0
    def sumNumbers(self, root):
        def subsum(root, val):
            if root.left == None and root.right == None:
                self.sum += val * 10 + root.val
            if root.left != None:
                subsum(root.left, val * 10 + root.val)
            if root.right != None:
                subsum(root.right, val *10 + root.val)
        if root == None:
            return 0
        subsum(root, 0)
        return self.sum
        

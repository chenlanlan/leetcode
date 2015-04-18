#!/user/bin/python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a integer
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        leftdepth = self.minDepth(root.right)
        rightdepth = self.minDepth(root.left)
        if leftdepth == 0:
            return rightdepth + 1
        elif rightdepth == 0:
            return leftdepth + 1
        else:
            return min(leftdepth, rightdepth) + 1
        

#!/user/bin/python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        ans = []
        def appendval(self, root):
            if root = None:
                return ans
            ans.append(self.val)
            self.appendval(self.left)
            self.appendval(self.right)

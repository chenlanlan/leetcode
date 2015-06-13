# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if root == None:
            return 0
        rightHeight = self.rightH(root)
        leftHeight = self.leftH(root)
        if rightHeight == leftHeight:
            return 2 ** rightHeight - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def rightH(self, root):
        count = 1
        while root.right:
            count += 1
            root = root.right
        return count

    def leftH(self, root):
        count = 1
        while root.left:
            count += 1
            root = root.left
        return count
                
        

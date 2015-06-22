#!/usr/bin/python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        res = []
        if not root:
            return res
        curLevel = 1
        nextLevel = 0
        queue = [root]
        while queue:
            cur = queue[0]
            del queue[0]
            curLevel -= 1
            if cur.left:
                queue.append(cur.left)
                nextLevel += 1
            if cur.right:
                queue.append(cur.right)
                nextLevel += 1
            if curLevel == 0:
                res.append(cur.val)
                curLevel = nextLevel
                nextLevel = 0
        return res

            

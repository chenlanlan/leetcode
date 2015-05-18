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
        ans = []
        if root == None:
            return ans
        queue = []
        queue.append(root)
        curLevel = 1
        nextLevel = 0
        while queue != []:
            cur = queue[0]
            del queue[0]
            curLevel -= 1
            if cur.left:
                queue.append()
                nextLevel += 1
            if cur.right:
                queue.append()
                nextLevel += 1
            if curLevel == 0:
                ans.append(cur.val)
                curLevel = nextLevel
                nextLevel = 0
        return ans

            

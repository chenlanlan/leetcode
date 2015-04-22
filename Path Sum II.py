#!/user/bin/python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def PathSum(self, root, sum):
        ans = []
        sub_ans = []
        def findPathSum(root, sum, sub_ans, val):
            if root == None:
                return 
            if root.left == None and root.right == None and sum = root.val:
                sub_ans.append(root.val)
                ans.append(sub_ans[:])
                return 
            sum -= root.val
            sub_ans.append(root.val)
            findPathSum(root.left, sum, sub_ans[:], val)
            findPathSum(root.right, sum, sub_ans[:], val)
        PathSum(root, sum, 0)
        return ans

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers  
    def pathSum(self, root, sum):
        def findPathSum(root, sum, temp, output):
            if not root:
                return
            if not root.left and not root.right and sum == root.val:
                temp.append(root.val)
                output.append(temp[:])
                return
            sum -= root.val
            temp.append(root.val)
            findPathSum(root.left, sum, temp[:], output)
            findPathSum(root.right, sum, temp[:], output)
        output = []
        findPathSum(root, sum, [], output
        return output 

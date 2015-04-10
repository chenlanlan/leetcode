#!/user/bin/python

def hasPathSum(self, root, sum):
    def PathSum(root, sum, val):
        if root == None:
            return False
        val += root.val
        if root.left == None and root.right == None:
            if sum == val:
                return True
            else:
                return False
        return PathSum(root.left, sum, val) or PathSum(root.right, sum, val)
    return PathSum(root, sum, 0)

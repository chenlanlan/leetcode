#!/user/bin/python

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        res = 0
        length = len(A)
        for i in range (0, length):
            if A[i] == elem:
                res +=1
            elif res > 0:
                A[i - res] = A[i]
        return length -res

x = Solution()
print(x.removeElement([1, 3, 4, 3, 5, 3], 5))

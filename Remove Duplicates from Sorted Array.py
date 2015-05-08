#!/usr/bin/python

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        j = 0
        res = 0
        for i in range (0, n - 1):
            if A[j] == A[i + 1]:
                res += 1
            elif res > 0:
                A[i - res + 1] = A[i + 1]
                j = i + 1
            else:
                j = i + 1
        return n - res

x = Solution()
print(x.removeDuplicates([1, 1, 2, 2, 2, 3]))

class Solution:
    # @param a list of integers
    # @return an integer           
    def removeDuplicates2(self, A):
        n = len(A)
        if n == 0:
            return 0
        i = 1
        j = 1
        while i < n:
            if A[i] != A[j - 1]:
                A[j] = A[i]
                j += 1
            i += 1
        return j


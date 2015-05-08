#!/usr/bin/python

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        b = []
        rel = []
        for i in range (0, numRows):
            a = []
            for j in range (0, i+1):
                if j == 0 or j == i:
                    a.append(1)
                else:
                    a.append(b[j-1] + b[j])
            rel.append(a)
            b = list(a)
        return rel
        
x = Solution()
print(x.generate(3))

class Solution:
    # @return a list of lists of integers
    def generate2(self, rowIndex):
        numRows = rowIndex + 1
        rel = []
        a = []
        for i in range (1, numRows + 1):
            for j in range (i , 0, -1):
                if j == i:
                    a.append(1)
                elif j != 1:
                    a[j - 1] = a[j - 1] + a[j - 2]
            rel.append(a[:])
        return rel[numRows - 1]


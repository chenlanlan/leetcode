#!user/bin/python

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
        
self = 0
numRows = 3
print(generate(self, numRows))

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
self = 0
rowIndex = 0
print(generate2(self, rowIndex))

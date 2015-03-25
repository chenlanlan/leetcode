#!/user/bin/python

def removeElement(self, A, elem):
    res = 0
    length = len(A)
    for i in range (0, length):
        if A[i] == elem:
            res +=1
        elif res > 0:
            A[i - res] = A[i]
    print (A)
    return length -res

self = 0
elem = 5
A= [1, 3, 4, 3, 5, 3]
print(removeElement(self, A, elem))

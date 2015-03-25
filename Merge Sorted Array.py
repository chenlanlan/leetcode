#!/user/bin/python

def merge(self, A, m, B, n):
    k = m + n
    i = m - 1
    j = n - 1
    print (i)
    for h in range (0, n):
        A.append(0)
        print(A)
    while j >= 0:
        for k in range(m + n -1, -1, -1):
            if B[j] < A[i] and i >= 0 :
                A[k] = A[i]
                i -= 1
            elif j >= 0:
                A[k] = B[j]
                j -= 1
    return A

self = 0
A = [2, 7, 9, 13, 17]
m = 5
B = [5]
n = 1
print(merge(self, A, m, B, n))



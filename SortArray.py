#!/usr/bin/python

def sortedArray(Array):
    length = len(Array)
    p = 0
    r = length - 1
    def merge(A, p, q, r):
        n1 = q - p + 1
        n2 = r - q
        L = []
        R = []
        for i in range(0, n1):
            L.append(A[p + i])
        for j in range(0, n2):
            R.append(A[q + 1 + j])
        #L.append(float('inf'))
        #R.append(float('inf'))
        i = 0
        j = 0
        for k in range(p, r + 1):
            if i < n1 and j < n2:
                if L[i] < R[j]:
                    A[k] = L[i]
                    i += 1
                else:
                    A[k] = R[j]
                    j += 1
            elif j == n2:
                A[k] = L[i]
                i += 1
            elif i == n1:
                A[k] = R[j]
                j += 1
        return
    def merge_sort(Array, p, r):
        if p < r:
            q = (p + r) //2
            merge_sort(Array, p, q)
            merge_sort(Array, q + 1, r)
            merge(Array, p, q, r)
        return
    merge_sort(Array, p, r)
    return Array
    
Array = [5,1,2,6,3]
print(sortedArray(Array))

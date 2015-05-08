#!/usr/bin/python

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        size = len(A)
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
                L.append(float('inf'))
                R.append(float('inf'))
                i = 0
                j = 0
                for k in range(p, r + 1):
                    if L[i] < R[j]:
                        A[k] = L[i]
                        i += 1
                    else:
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
        sortedArray(A)
        for h in range(size - 1, -1, -1):
            if A[h] == elem:
                del A[h]
                size -= 1
        return size

x = Solution()
print(x.removeElement([2], 2))

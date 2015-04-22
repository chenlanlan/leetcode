#!/user/bin/python

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing(void)
    def merge(self, A, m, B, n):
        k = m + n
        i = m - 1
        j = n - 1
        for h in range (0, n):
            A.append(0)
        while j >= 0:
            for k in range(m + n -1, -1, -1):
                if B[j] < A[i] and i >= 0 :
                    A[k] = A[i]
                    i -= 1
                elif j >= 0:
                    A[k] = B[j]
                    j -= 1
        return A

x = Solution()
print(x.merge([2, 7, 9, 13, 17], 5, [5], 1))



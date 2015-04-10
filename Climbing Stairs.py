#!/user/bin/python

def climbStairs(self, n):
    if n == 1:
        return 1
    F = []
    for i in range(n):
        F.append(0)
    F[0] = 1
    F[1] = 2
    for i in range(2, n):
        F[i] = F[i - 1] + F[i - 2]
    return F[n - 1]

self = 0
n = 1
print (climbStairs(self, n))

#!/user/bin/python

def rob(self, num):
    n = len(num)
    if n == 0:
        return 0
    elif n == 1:
        return num[0]    
    d = []
    for i in range(n):
        d.append(0)
    d[0] = num[0]
    d[1] = max(num[0], num[1])
    for i in range(2,n):
        d[i] = max((d[i - 2] + num[i]), d[i - 1])
    return d[n - 1]

self = 0
num = [2,1]
print(rob(self, num))

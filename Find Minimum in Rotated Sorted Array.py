#!/user/bin/python

def findMin(self, num):
    n = len(num)
    left = 0
    right = n - 1
    while left < right:
        if num[left] < num[right]:
            return num[left]
        mid = (left + right) // 2
        if num[mid] < num[left]:
            right = mid
        else:
            left = mid + 1 
    return num[left]

self = 0
num = [4, 1, 4, 4, 4]
print(findMin(self, num))

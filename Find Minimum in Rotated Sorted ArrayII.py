#!/user/bin/python

def findMin(self, num):
    n = len(num)
    left = 0
    right = n - 1
    while left < right:
        if num[left] < num[right]:
            return num[left]
        mid = left + (right - left) // 2
        if num[left] == num[mid]:
            if left + 1 == right:
                if num[left] >= num[right]:
                    left = right
                    break
            else:
                left += 1
            
        elif num[mid] > num[left]:
            left = mid
        else:
            right = mid 
    return num[left]

self = 0
num = [1, 1]
print(findMin(self, num ))

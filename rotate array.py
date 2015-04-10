#!/user/bin/python
def rotate(self, nums, k):
    length = len(nums)
    step = k % length
    def reverse(i, j, Array):
        while i<j:
            temp = Array[i]
            Array[i] = Array[j]
            Array[j] = temp
            i +=1
            j -=1
        return Array
    print(reverse(0, length - step - 1, nums))
    print(reverse(length - step, length - 1, nums))
    reverse(0, length - 1, nums)
    return nums
self = 0
nums = [1]
print (rotate(self, nums, 0))
            
            

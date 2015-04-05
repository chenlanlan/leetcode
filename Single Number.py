#!/user/bin/python

def singleNumber(self, A):
    n = len(A)
    for i in range(n):
        if i == 0 and  (not A[i] in A[i+1:]):
            return A[i]
        elif (not A[i] in A[0:i]) and (not A[i] in A[i+1:]):
            return A[i]
self = 0
A = [4, 5, 6, 3, 5, 6, 3]
print(singleNumber(self, A))
            
                        
def singleNumber2(self, A):
    n = len(A)
    single_num = 0
    for i in range(n):
        single_num ^= A[i]
    return single_num
self = 0
A = [4, 5, 6, 3, 5, 6, 3]
print(singleNumber(self, A))

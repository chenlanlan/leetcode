#!user/bin/python

def majorityElement(self, num):
    n = len(num)
    number_of_majority = 0
    for i in range(0, n):
        sum_i = 1
        for j in range (i+1, n):
            if num[i] == num[j]:
                sum_i = sum_i + 1
        number = sum_i
        if number > number_of_majority:
            number_of_majority = number
    return number_of_majority

num = [3, 5, 6, 4, 3, 5, 66, 66, 66, 66, 4, 4]
self = 0
print(majorityElement(self, num))

import random
def majorityElement2(self, num):
    n = len(num)
    number_of_majority = 0
    if n == 1:
        number_of_majority = 1
    while number_of_majority <= n / 2:
        i = random.randint(0, n-1)
        number = 0
        for j in range (0, n):
            if num[i] == num[j]:
                number +=1
            if number > n / 2:
                number_of_majority = number
    return number_of_majority

test = [3, 3, 2, 4, 3, 9, 11, 3, 5, 3, 3, 3]
self = 0
print(majorityElement2(self, test))

def majorityElement3(self, num):
    candidate, count = None, 0
    for e in num:
        if count == 0:
            candidate, count = e, 1
        elif e == candidate:
            count += 1
        else:
            count -= 1
    return candidate

test1 = [3, 3, 2, 4, 3, 9, 11, 3, 5, 3, 3, 3, 3]
self = 0
print(majorityElement3(self, test1))
        
        

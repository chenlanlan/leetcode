#!/user/bin/python

def trailingZeroes(self, n):
    number_of_5 = 0
    x = 5
    while x <= n:
        number_of_5 += n // x
        x *= 5
    number_of_zeroes = number_of_5
    return number_of_zeroes

self = 0
n = 28
print (trailingZeroes(self, n))


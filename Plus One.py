#!/user/bin/python

def plusOne(self, digits):
    size = len(digits)
    if digits[size - 1] < 9:
        digits[size - 1] = digits[size - 1] + 1
        return digits
    if size == 1 and digits[0] == 9:
        digits[0] = 0
        digits.insert(0,1)
        return digits
    for i in range(size - 1, -1, -1):
        digits[i] = 0
        digits[i - 1] += 1
        if digits[i - 1] <= 9:
            break
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0,1)
            break
    return digits
        
self = 0
digits = [9]
print(plusOne(self, digits))

def plusOne2(self, digits):
    size = len(digits)
    carry = True
    for i in range(size - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            carry = False
            break
    if carry == True:
        digits.insert(0, 1)
    return digits
self = 0
digits = [9, 9]
print(plusOne2(self, digits))

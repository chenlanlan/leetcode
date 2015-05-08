#!/usr/bin/python

def standingovation(smax, s):
    output = 0
    num = 0
    for i in range(int(smax) + 1):
        if i > num and s[i] != 0:
            output += i - num
            num += i - num
        num += int(s[i])
    return output


f = open('A-small-attempt1.in')
file = open('Output.txt', 'w')
t = int(f.readline())
for _t in range(t):
    input_s = f.readline().split()[1:]
    smax = len(input_s[0]) - 1
    n = standingovation(smax, input_s[0])
    file.write("Case #%d: %d" % (_t+1, n) + '\n')
    
    #print ("Case #%d: %d" % (_t+1, n))
f.close()
file.close()




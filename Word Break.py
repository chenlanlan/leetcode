#!/user/bin/python

def wordBreak(self, s, dict):
    global Find
    begin = 0
    end = len(s)
    Find = False
    if s in dict:
        return True
    def find_word(begin, end, dict):
        global Find
        if Find == True:
            return
        if begin >= end:
            Find = True
            return
        for i in range (begin, end):
            temp = begin
            print (s[begin : i + 1], i)
            if s[begin : i + 1] in dict:
                
                temp = i + 1
                find_word(temp, end ,dict)
                print('begin, end:',begin,end,Find)
    find_word(begin, end, dict)
    return Find

self = 0
s = 'aaaaaaa'
dict = ['aa', 'aaaaa','aaa']
print(wordBreak(self, s, dict))

def wordBreak2(self, s, dict):
    n = len(s)
    F = []
    for i in range(n + 1):
        F.append(False)
    if s[0] in dict:
        F[0] = True
    for i in range (1, n + 1):
        for j in range (0, i):
            if F[j]==True and s[j + 1 : i + 1] in dict:
                F[i] = True
            elif s[0 : i + 1] in dict:
                F[i] = True
        print('i, F', i, F[i])
    return F[n]
self = 0
s = 'aaaaaaa'
dict = ['aa', 'aaaa','oo']
print(wordBreak2(self, s, dict))
            

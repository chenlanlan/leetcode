#!/user/bin/python

def compareVersion(self, version1, version2):
    v1 = version1.split('.')
    v2 = version2.split('.')
    len1 = len(v1)
    len2 = len(v2)
    len_max = max(len1, len2)
    for i in range (len_max):
        v1_taken = 0
        if i < len1:
            v1_taken = int(v1[i])
        v2_taken = 0
        if i < len2:
            v2_taken = int(v2[i])
        if v1_taken > v2_taken:
            return 1
        if v1_taken < v2_taken:
            return -1
    return 0
   
self = 0
version1 = '1.3.3'
version2 = '2.2'
print(compareVersion(self, version1, version2))

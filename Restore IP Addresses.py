#!/usr/bin/python

class Solution:
    # @param {string} s
    # @return {string[]}
    def isValid(self, num):
        if len(num) == 1 and num >= '0' and num <= '9': return True
        if len(num) == 2 and num >= '10' and num <= '99': return True
        if len(num) == 3 and num >= '10' and num <= '255': return True
        return False
        
    def restoreIp(self, result, ips, kth, start, s):
        if start == len(s):
            if kth == 5:
                ip = ips[0]
                for i in range(1, 4):
                    ip += '.' + ips[i]
                result.append(ip)
        k = 1
        while k <= 3 and start + k - 1 < len(s):
            num = s[start: start + k]
            if self.isValid(num):
                ips.append(num)
                self.restoreIp(result, ips, kth + 1, start + k, s)
                ips.pop()
            k += 1
        
    def restoreIpAddresses(self, s):
        result = []
        if len(s) < 4 or len(s) > 12:
            return result
        ips = []
        self.restoreIp(result, ips, 1, 0, s)
        return result

test = Solution()
print(test.restoreIpAddresses('25525511135'))
    

#!/usr/bin/python

import math
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        ans = 1
        def isPrimes(num):
            if num == 1:
                return False
            s = int(math.sqrt(num))
            for j in range(s, 1, -1):
                if num % j == 0:
                    return False
            return True
        if n == 1 or n == 2:
            return 0
        elif n == 3:
            return 1
        else:
            for i in range(3, n, 2):
                if isPrimes(i):
                    ans += 1
            return ans
        
    def countPrimes2(self, n):
        ans = [2, 3]
        if n == 1 or n == 2:
            return 0
        elif n == 3:
            return 1
        elif n == 4:
            return 2
        else:
            for i in range(5, n, 2):
                app = True
                for j in range(0, len(ans)):
                    if i % ans[j] == 0:
                        app = False
                        break
                if app:
                    ans.append(i)
            return len(ans)

    def countPrimes(self, n):
        if n <= 2:
            return 0
        ans = [i for i in range(0, n)]
        res = len(ans) - 2
        j = 2
        while j < n:
            if ans[j] != 0:
                if j * j > n:
                    break
                current = 2 * j
                while current < n:
                    if ans[current] != 0:
                        ans[current] = 0
                        res -= 1
                    current += j
            j += 1
        return res        
        
x = Solution()
#print(x.countPrimes(1500000))
#print(x.countPrimes2(1500000))
print(x.countPrimes3(1500000))


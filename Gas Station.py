#!/usr/bin/python

class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        tan = 0
        stationPassed = 1
        head = 0
        for i in range(len(gas)):
            tan = tan - cost[i] + gas[i]
            if tan < 0:
                tan = 0
                head = i + 1
        if head >= len(gas):
            return -1
        index = head
        tan = 0
        while stationPassed <= len(gas) and tan >= 0:
            tan = tan - cost[head] + gas[head]
            head = (head + 1) % len(gas)
            stationPassed += 1
        if tan < 0:
            return -1
        return index
               
test = Solution()
gas = [2, 3, 4, 5, 6]
cost = [6, 11, 4, 1, 1]
print(test.canCompleteCircuit(gas, cost))


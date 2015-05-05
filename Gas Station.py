#!/user/bin/python

class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost): #Memory limit exceeded
        def findIndex(gas, cost, index):
            if index == len(gas):
                return -1
            gas = change(gas, index)
            cost = change(cost, index)
            print (gas, cost)
            if determine(gas, cost):
                return index
            else:
                index += 1
                return findIndex(gas, cost, index)
        
        def change(A, index):
            if index == 0:
                return A
            else:
                res = A[1 : len(A)]
                res.append(A[0])
                return res

        def determine(gas, cost):
            tan = gas[0]
            for i in range(1, len(gas)):
                if tan - cost[i - 1] >= 0:
                    tan = tan - cost[i - 1] + gas[i]
                else:
                    return False
            if tan - cost[-1] >= 0:
                return True
            else:
                return False
        return findIndex(gas, cost, 0)
    
    def canCompleteCircuit2(self, gas, cost):
        tan = 0
        stationPassed = 1
        head = 0
        for i in range(0, len(gas)):
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
print(test.canCompleteCircuit2(gas, cost))

#!/user/bin/python

def maxProfit(self, prices):
    if len(prices) == 0:
        return 0
    ans = 0
    n = len(prices)

    opt = [0 for i in range(n)]
    lowest = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] < lowest:
            lowest = prices[i]
        elif prices[i] - lowest > profit:
            profit = prices[i] - lowest
        opt[i] = profit

    optReverse = [0 for i in range(n)]
    highest = prices[n - 1]
    profit = 0
    for i in range(n - 2, 0, -1):
        if prices[i] > highest:
            highest = prices[i]
        elif highest - prices[i] > profit:
            profit = highest - prices[i]
        optReverse[i] = profit

    for i in range(n):
        add = opt[i] + optReverse[i]
        if add > ans:
            ans = add
    return ans

self = 0
prices = [5, 1, 2, 4, 3, 6]
print(maxProfit(self, prices))


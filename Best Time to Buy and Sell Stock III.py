#!/user/bin/python

def maxProfit3(self, prices):
    if len(prices) == 0:
        return 0
    ans = 0
    n = len(prices)

    opt = [0 for i in range(n)]
    min = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] < min:
            min = prices[i]
        elif prices[i] - min > profit:
            profit = prices[i] - min
        opt[i] = profit

    optReverse = [0 for i in range(n)]
    max = prices[n - 1]
    profit = 0
    for i in range(n - 2, 0, -1):
        if prices[i] > max:
            max = prices[i]
        elif max - prices[i] > profit:
            profit = max - prices[i]
        optReverse[i] = profit

    for i in range(n):
        add = opt[i] + optReverse[i]
        if add > ans:
            ans = add
    return ans

self = 0
prices = [5, 1, 2, 4, 3, 6]
print(maxProfit2(self, prices))


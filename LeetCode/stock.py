class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) < 2:
            return 0
        buyP = sellP = prices[0]
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > buyP:
                sellP = prices[i]
                res = max(res, sellP - buyP)
            buyP = min(buyP, prices[i])
        return res


prices = [7, 1, 5, 3, 6, 4]
print(Solution.maxProfit([], prices))

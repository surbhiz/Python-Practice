class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(prices[a+1] - prices[a] for a in range(len(prices)-1) if prices[a] < prices[a+1])


prices = [1, 2, 3, 4, 5]
print(Solution.maxProfit([], prices))

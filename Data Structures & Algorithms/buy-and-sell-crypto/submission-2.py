class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        hist = set()
        for x in range(len(prices)):
            hist.add(prices[x])
            temp = prices[x] - min(hist)
            profit =  max(profit, temp)
        return profit
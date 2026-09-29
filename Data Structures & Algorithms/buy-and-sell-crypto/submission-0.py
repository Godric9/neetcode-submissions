class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        maxOut = 0
        i = len(prices) - 1
        while i > 0:
            out = prices[i]
            prices.pop(i)
            maxOut = max(maxOut, out - min(prices))
            i -= 1
        return maxOut
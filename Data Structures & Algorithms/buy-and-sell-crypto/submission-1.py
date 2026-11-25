class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        maxprof = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j]-profit[i]
                maxprof = max(profit,maxprof)
            else:
                l = r
            r += 1
        
        return 

        
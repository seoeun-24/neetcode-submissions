class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #so the first price should be lower than latter one to make the profit.
        profit =0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i]>profit:
                    profit = prices[j]-prices[i]
        return profit



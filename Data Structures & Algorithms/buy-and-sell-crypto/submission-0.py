class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min=float('inf')
        best_profit=0
        for i in range(len(prices)):
            best_profit=max(best_profit, prices[i]-curr_min)
            curr_min=min(curr_min, prices[i])
        return best_profit


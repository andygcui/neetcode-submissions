class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = 0
        best_profit = 0

        for i in range(len(prices)):
            current_profit = prices[i] - prices[current_min]
            if current_profit > best_profit:
                best_profit = current_profit
            
            if prices[i] < prices[current_min]:
                current_min = i
        
        return best_profit



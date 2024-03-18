class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = 10001
        max_value = -1
        for i in range( len(prices)):
            if min_value > prices[i]:
                min_value = prices[i]
                max_value = -1
                continue
            elif max_value < prices[i]:
                if max_profit > prices[i] - min_value:
                    continue
                max_value = prices[i]
                max_profit = prices[i] - min_value
                continue
        return max_profit
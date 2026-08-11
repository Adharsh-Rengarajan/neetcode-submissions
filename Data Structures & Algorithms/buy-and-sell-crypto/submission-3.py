class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = 101

        for i in prices:
            max_profit = max(max_profit, i-min_value)
            min_value = min(i, min_value)

        return max_profit
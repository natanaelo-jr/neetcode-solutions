class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_index = 0
        sell_value = 0

        for i in range(len(prices)):
            if prices[buy_index] > prices[i]:
                buy_index = i
            if prices[i] - prices[buy_index] > sell_value:
                sell_value = prices[i] - prices[buy_index]

        return sell_value
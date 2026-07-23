class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # not_holding: max profit when not holding stock
        # holding: max profit when holding stock
        not_holding = 0
        holding = -prices[0]

        for i in range(1, len(prices)):
            new_not_holding = max(not_holding, holding + prices[i])
            new_holding = max(holding, not_holding - prices[i])
            not_holding = new_not_holding
            holding = new_holding

        return not_holding
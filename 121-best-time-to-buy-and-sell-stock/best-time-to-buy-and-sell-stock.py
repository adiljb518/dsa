class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ##Incorrect
        # m=min(prices)
        # min_indx=prices.index(m)
        # prices[:]=prices[min_indx:]
        # max_value=max(prices)
        # profit=max_value-m
        # return profit
        ##correct
        buy_price = prices[0]
        profit = 0
        for i in range(len(prices)):
            # if prices[i]<buy_price:
            #     buy_price=prices[i]
            buy_price = min(buy_price,prices[i])
            # curr_profit = prices[i]-buy_price
            # if curr_profit>profit:
            #     profit = curr_profit
            profit = max(profit,prices[i]-buy_price)
        return profit

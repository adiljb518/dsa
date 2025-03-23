class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy_price = prices[0]
        # profit = 0
        # for i in range(n):
        #     if num[i] < buy_price:
        #         buy_price = nums[i]
        #         break
        # sell_price = nums[i]
        # for j in range(i+1,n):
        #     if nums[j] > nums[j+1]:
        #         sell_price = nums[j]
        #         break
        #     else:
                
        # profit = sell_price-buy_price
        profit = 0
        n =len(prices)
        for i in range(1,n):
            if prices[i] > prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit



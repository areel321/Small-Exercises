'''
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=problem-list-v2&envId=dynamic-programming
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price = prices[0] # start buying at first price
        profit = 0
        # if we encounter a smaller buy_price, buy that one
        # if we get a larger profit, sell on that day

        for i in prices:
            if i < buy_price:
                buy_price = i
            
            if i - buy_price > profit:
                profit = i - buy_price
            
            
        return profit
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        greatestPrice = 0
       
        for left in range(0,len(prices)-1):
            for right in range(left+1,len(prices)):
                greatestPrice = max(prices[right]-prices[left], greatestPrice)
                if greatestPrice > 0:
                    print(left, right)
            
            
            
        return greatestPrice
'''

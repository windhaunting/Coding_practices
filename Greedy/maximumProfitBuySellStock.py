#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 23:12:58 2018

@author: fubao
"""

# buy and sell series problem

# 714. Best Time to Buy and Sell Stock with Transaction Fee;        facebook

'''
#  Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.


Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.

'''



# reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/

# reference: http://hanslen.me/2017/10/15/Best-Time-to-Buy-and-Sell-Stock-series-with-Dynamic-Programming-in-Java/

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        #1st naive way is to check all the possible combinations to calculate the profit and then the maximum profit
        # consider the current cash
        # time complexity is O(n^2)
        
     
        
        #2rd intuitive way
        cash = 0
        hold= -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i]- fee)  # sell stocks
            hold = max(hold, cash - prices[i])       # buy stocks
            
        return cash
    
    

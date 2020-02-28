#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 11:27:32 2018

@author: fubao
"""

# 121. Best Time to Buy and Sell Stock
'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''


def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # 1st iterate first round, get the index i of minimum number, then find the maximum number from the index i+1 
    
    #2nd get the maximum gap max(prices[i]-prices[j]) i > j
    
    curMax = 0
    ansMax = 0
    for i in range(1, len(prices)):
        curMax = max(0, curMax + prices[i]-prices[i-1])
        ansMax = max(curMax, ansMax)
        print ("curMax: ", curMax, ansMax)
    return ansMax


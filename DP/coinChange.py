# -*- coding: utf-8 -*-
"""
Created on Thu May 31 22:03:13 2018

@author: Fubao.Wu
"""

'''
322. Coin Change
DescriptionHintsSubmissionsDiscussSolution
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.
'''

def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    
    #method 1: using recursive: count(coins, amount) =  1 + min(count(coins, amount - coins[i])) for i from 0 to len(coins)
    
    if amount == 0:
        return 0
    ans = sys.maxsize
    
    for i in range(0, len(coins)):
        if coins[i] <= amount:
            tmp = coinChange(coins, amount - coins[i])
            if tmp != -1 and tmp + 1 < ans:
                ans = tmp + 1
            print ("ttttttttt")
    return ans if ans != sys.maxsize else -1
        
coins =[1,2,5]
amount = 100
coinChange(coins, amount)



def coinChange2(coins, amount):

  #2 use DP to optimize;     memoization; dp[i] indicate the minimum number of coins for i value
        dp = [0] * (amount + 1)
        for i in range(1, amount+1):
            dp[i] =  sys.maxsize
        
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    tmp = dp[i-coins[j]]
                    if tmp != -1 and tmp + 1 < dp[i]:
                        dp[i] = tmp + 1
        return dp[amount]  if dp[amount]  != sys.maxsize else -1
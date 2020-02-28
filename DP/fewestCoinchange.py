#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:09:32 2018

@author: fubao
"""



# 322. Coin Change 硬币找零   518. Coin Change 2


'''
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.

'''
'''
Let dp[v] to be the minimum number of coins required to get the amount v. 
dp[i+a_coin] = min(dp[i+a_coin], dp[i]+1) if dp[i] is reachable. 
dp[i+a_coin] = dp[i+a_coin] is dp[i] is not reachable. 
We initially set dp[i] to be MAX_VALUE. 


or 

dp[i] = min(dp[i], dp[i - coins[j]] + 1);
其中coins[j]为第j个硬币，而i - coins[j]为钱数i减去其中一个硬币的值，
剩余的钱数在dp数组中找到值，然后加1和当前dp数组中的值做比较，取较小的那个更新dp数组。
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        '''
        
        dp[i] = min(dp[i], dp[i - coins[j]] + 1);
        其中coins[j]为第j个硬币，而i - coins[j]为钱数i减去其中一个硬币的值，
        剩余的钱数在dp数组中找到值，然后加1和当前dp数组中的值做比较，取较小的那个更新dp数组。

        '''
        
        #1st first us DP 
        
        rs = [amount+1] * (amount+1)
        rs[0] = 0
        for i in xrange(1, amount+1):
            for c in coins:
                if i >= c:
                    rs[i] = min(rs[i], rs[i-c] + 1)

        if rs[amount] == amount+1:
            return -1
        return rs[amount]
        
        
        
        #2nd use BFS
        '''
         find the least coin solution (like a shortest path from 0 to amount),
        using BFS gives results much faster than DP.

        inspired by the BFS solution for problem Perfect Square
        '''
        
        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc =  0
        visited = [False]*(amount+1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    newval = v + coin
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:
                        visited[newval] = True
                        value2.append(newval)
            value1, value2 = value2, []
        return -1
    
        

'''

# 518. Coin Change 2


2. 
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Note: You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
 

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
 

比如可能由每种硬币单独来组成，或者是两种硬币同时来组成。那么我们怎么量化呢，
比如我们有两个硬币[1,2]，钱数为5，那么钱数的5的组成方法是可以看作两部分组成，
一种是由硬币1单独组成，另一种是此时我们如果取出一个硬币2，相当于由硬币[1,2]组成的钱数为3的总方法。
是不是不太好理解，多想想。那么我们的需要一个二维的dp数组，其中dp[i][j]表示用前i个硬币组成钱数为j的不同组合方法，那么我们的递推公式也在上面的分析中得到了：

dp[i][j] = dp[i - 1][j] + (j >= coins[i - 1] ? dp[i][j - coins[i - 1]] : 0)

'''



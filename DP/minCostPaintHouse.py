#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 18:00:31 2018

@author: fubao
"""



#  Paint House I

'''
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
 For example, costs[0][0] is the cost of painting house 0 with color red; 
 costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

'''

# Use DP to solve this question

# define DP[i][j] is the cost with the i's house and j's color;
#if the current house painted with color j, the current cost is the current cost with color j and the previous cost with one of two different colors.:

# DP[i][j] = DP[i][j] + min(DP[i-1][(j+1)%3], DP[i-1][(j+2)%3])

def minCost(costs):
    """
    :type costs: List[List[int]]
    :rtype int
    """
    
    if not costs:
        return 0
    n = len(costs)
    dp = costs   # [[0 for i in range(0, 3)] for i in range(0, n)]
    
    for i in range(1, n):
        for j in range(0, 3):
            dp[i][j] += min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])
            
        
    print("dp: ", dp)
    
    return min(dp[n-1])
costs= [[3,5,4],[1,2,3]]

print ("ans: ", minCost(costs))




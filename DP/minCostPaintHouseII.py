#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 19:04:13 2018

@author: fubao
"""

# Paint house II

'''
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain 
color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n*k cost matrix. For example, costs[0][0] is the cost of 
painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost
to paint all houses.

Note:
All costs are positive integers.

Follow up: Could you solve it in O(nk) runtime.

'''

'''
#1st Here we have k colors, if we use the same method as the previous method, there probably would have TLE problem
# define DP[i][j] is the cost with the i's house and j's color;
#if the current house painted with color j, the current cost is the current cost with color j and the previous cost with one of two different colors.:

# DP[i][j] = DP[i][j] + min(DP[i-1][(j+1)%k], DP[i-1][(j+2)%k],...)


this would take O(nk) space, but O(nk*k) time complexity

#2nd how to use O(n*k) time complexity?


There are two options:
1st; when the current house color is i, the previous house color must be not i, but the minimum cost corresponds to i, so select the second minimum cost that does not correspond i;
2nd; when the current house color is i, the previous house color must be not i, the minimum cost does not correspond to i, so selec the minimum cost that has color j
Therefore, we maintain two minimum cost, 1st is the minimum cost and the lastColor, 2nd is the second minimum cost 
'''

# reference:  https://zhengyang2015.gitbooks.io/lintcode/paint_house_ii_516.html
'''
的方法，更新当前行的某个值时需要搜索上一行和当前不同列的所有可能，
则当k很大时，会十分耗费时间。因此，可以不能直接用I中的方法，需要优化。

优化的方法为：
只记录3个值，即前一行最小值，第二小值，和最小值的index。
更新当前行元素，当前行元素记录的是当前行房子涂该种颜色时的最小值，
只可能由该元素与上一行的最小值或次小值加和得到。遍历当前行的每个元素，若该元素的列和前一行最小值index不同，则更新为当前行元素值＋上一行最小值，若和上一行最小值index相同，则更新为当前元素值＋上一行次小值。同时将该值和当前行的最小值和次小值比较，更新当前行的最小值，次小值和最小值的index。
重复2直到遍历所有行。

'''

def minCostII(costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    if not costs:
        return 0
    
    #dp = costs
    
    n = len(costs)
    k = len(costs[0])
    preMin = 0
    preSecMin = 0
    preInd = 0
    
    for i in range(0, n):
        curMin = 2**32
        curSecMin = 2**32
        curInd = -1
        
        for j in range(0, k):
            if j == preInd:
                # use second 
                costs[i][j] += preSecMin
            else:
                costs[i][j] += preMin
            
            #update the current min, second min
            if costs[i][j] < curMin:
                curSecMin = curMin
                curMin = costs[i][j]
                curInd = j
            elif costs[i][j] < curSecMin:
                curSecMin = costs[i][j]
        preMin = curMin
        preSecMin = curSecMin
        preInd = curInd

    return preMin

costs= [[3,5,4,3],[1,2,3,2]]

print ("ans: ", minCostII(costs))


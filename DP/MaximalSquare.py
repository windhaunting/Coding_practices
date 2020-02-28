#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 00:16:45 2018

@author: fubao
"""


'''

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

'''

# dp problem


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #1st brute force;  start each element and treat the element as the beginning element; then select 1*1, 2*2, 3*3,....
        # until the bound to check the square element are all 1. (enumerate all squares)

        
        #2nd there are lots of repetitions; accepted
        # use dp[i][j] indicate the square width/length with all 1 inside from the beginning point [0][0]
        
        # left, upper, left upper
        # dp[i][j]=min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        
        if matrix is None or len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for i in range(0, m)]
        
        print ("dp: ", dp)
        #dp[i][j] = 
        
        ans = 0
        
        for i in range(0, m):
            for j in range(0, n):
                dp[i][j] = int(matrix[i][j])
                if dp[i][j] == 0:
                    continue
                if i!=0 and j !=0:
                    dp[i][j] = min(min(dp[i-1][j-1], dp[i-1][j]), dp[i][j-1]) + 1
                
                ans = max(ans, dp[i][j]*dp[i][j])
                #print("i, j: ", i, j, ans, dp[i][j])
        return ans
    
        '''
        1 1 1
        1 1 0
        1 1 0
        '''
                
                
                
        

# ref:  # http://www.cnblogs.com/thoupin/p/4780352.html
# http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-221-maximal-square/


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:36:25 2018

@author: fubao
"""




# 62. Unique Paths


'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid 
(marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

'''



class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #SUCCESS 1st try :    DP： P[i][j] indicates how many unique path 
        # from src to P[i][j] P[i, j] = P[i-1][j] + P[i,j-1];  
        
      
        '''
        p = [[1 for i in range(n)] for j in range(m)]
        print ('p', p)
        for i in range(1, m):
            for j in range(1,n):
                p[i][j] = p[i-1][j] + p[i][j-1]
        return p[m-1][n-1]
        '''
        
        
        
        #2nd how to reduce the space to one dimension?
        # DP p[j] = p[j] +p[j-1]
        '''
        Further inspecting the above code, we find that keeping two columns 

        is used to recover pre[i], which is just cur[i] before its update. 
        So there is even no need to use two vectors and one is just enough.
        Now the space is further saved and the code also gets much shorter.
        we only need path[i - 1][j] (at the same column) and path[i][j - 1] (at the left column). 
        So it is enough to maintain two columns  (the current column and the left column) instead of maintaining
        the full m*n matrix.
        Now the code can be optimized to have O(min(m, n)) space complexity.
 
    '''
 
        p = [0 for i in range(0,n)]
        for i in range(0, m):
            p[0] = 1
            for j in range(1, n):
                p[j] = p[j] + p[j-1]
        return p[n-1]
        
        
        



 # 2nd if there is an obstacle:
 
 # https://leetcode.com/problems/unique-paths-ii/description/
 
 
 
 
 
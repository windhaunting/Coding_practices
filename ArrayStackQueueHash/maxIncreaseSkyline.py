#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 15:10:27 2018

@author: fubao
"""

# 807. Max Increase to Keep City Skyline

'''
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

'''


class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # find the pattern first;  every time we change a value in grid[i][j], find the possible value r it can change
        # what is the r? 
        m = len(grid)
        if grid is None or m == 0:
            return 0
        
        n = len(grid[0])
        ansSum = 0
        
        lrLst = []          #left and right view
        buLst = []          #bottom and top view
        for i in range(0, m):
            lrLst.append(max(grid[i]))
        
        for j in range(0, n):
            buLst.append(max([row[j] for row in grid]))
            
        print ("lrLst, buLst: ", lrLst, buLst)
        
        
        for i in range(0, m):
            for j in range(0, n):
                ansSum += min(lrLst[i], buLst[j])-grid[i][j] if min(lrLst[i], buLst[j]) > grid[i][j] else 0
        
        return ansSum



    
    '''
    more elegant writing from other's solution
    '''

    def maxIncreaseKeepingSkyline2(self, grid):
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]

        return sum(min(row_maxes[r], col_maxes[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))
        
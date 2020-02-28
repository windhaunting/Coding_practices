#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:46:16 2019

@author: fubao
"""


# facebook

'''
695. Max Area of Island
Medium

1306

65

Favorite

Share
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

'''


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #idea 1: recursively search and check it's island, if it is 1, then continue search it's 4-directions,
        #until we found connected island. we count and record the island number in the process
        
        if not grid:
            return 0
        count  = 0
        maxRes = 0
        #m = len(grid)
        #n = len(grid[0])
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1:
                    area = 0
                    area = self.dfsHelper(grid, i, j, area)
                    #print ("area: ", area)
                    maxRes = max(maxRes, area)
        return maxRes
    
    def dfsHelper(self, grid, i, j, area):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return area
        grid[i][j] = -1 # important to notice this
        area += 1
        #print ("areaxxxx:", area)
        area = self.dfsHelper(grid, i-1, j, area)
        area = self.dfsHelper(grid, i+1, j, area)
        area = self.dfsHelper(grid, i, j-1, area)
        area = self.dfsHelper(grid, i, j+1, area)
        return area

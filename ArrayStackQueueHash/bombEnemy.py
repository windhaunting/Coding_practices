#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 22:47:17 2018

@author: fubao
"""


#  [LeetCode] Bomb Enemy 炸弹人

'''
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)

'''




class Solution:
    # @param {character[][]} grid Given a 2D grid, each cell is either 'W', 'E' or '0'
    # @return {int} an integer, the maximum enemies you can kill using one bomb
    def maxKilledEnemies(self, grid):
        # Write your code here
        
        
        
        #1st naive algorithm get every position in the grid and search around four direction;
        # then get the max count of each got result  ;  time:  O(m*n*(m+n))   space:  O(1)
        
        
        
        #2nd optimized  reduce repeated compuation,  time:  O(m*n)   space:  O(n)
        
        m, n = len(grid), 0
        if m:
            n = len(grid[0])
        result, rows = 0, 0
        cols = [0 for i in range(n)]

        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == 'W':
                    rows = 0
                    for k in range(j, n):
                        if grid[i][k] == 'W':
                            break
                        if grid[i][k] == 'E':
                            rows += 1

                if i == 0 or grid[i-1][j] == 'W':
                    cols[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'W':
                            break
                        if grid[k][j] == 'E':
                            cols[j] += 1

                if grid[i][j] == '0' and rows + cols[j] > result:
                    result = rows + cols[j]

        return result

grid = [['0', 'E', '0', '0'], ['E','0','W','E'],['0', 'E', '0', '0']]

SolutionObj = Solution()
print("max count: ", SolutionObj.maxKilledEnemies(grid))


#  similar problem 
'''
intersection road cross
题目：矩阵中由1构成的一横一竖的连续的1，并且这一横一竖有一个交叉点的， 是一条十字路
总的来说对每一个1：  和他在同一列上，与他相连的的连续的1的数量 + 和同他在同一行上，与他相连的连续的1的数量 的和  就是以当前1为交叉点的十字路的长度
找出矩阵中最长的十字路。
. 1point3acres.com/bbs
举几个例子吧.

0 0 0. 
1 1 1
1 0 0   中最长的十字路长度是4

0 0 1 0 0 0. more info on 1point3acres.com
0 0 1 1 1 1
1 1 1 0 1 0
0 0 1 0 0 1
   中最长的十字路长度是7. 鐗涗汉浜戦泦,

'''
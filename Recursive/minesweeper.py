#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:26:44 2019

@author: fubao
"""

# facebook minesweeper

'''
529. Minesweeper
Medium

387

373

Favorite

Share
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
 

Example 1:

Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:

Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

'''

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        #SUCCESS case 1: if current pos is M, then assign it with X
        # case 2: if all 8 adjacent block has M, then count the number of M for each position if the count is not 0, assign the count to current pos; if te count is 0,then assin the pos with "B", then wee continue to find all its 8 adjacent blocks recursively.
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return board
    
        m = len(board)
        n = len(board[0])
        
        row = click[0]
        col = click[1]
        
        cnt = 0    # how many mines in the adjacent neighbors
        if board[row][col] == 'M':
            board[row][col] = 'X'
        
        else:
            # check all it 8 adjacent
            for i in range(-1, 2):
                for j in range(-1,2):
                    x = row + i
                    y = col + j
                    # out of boundary
                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    if board[x][y] == 'M':
                        cnt += 1
            if cnt > 0:
                board[row][col] = str(cnt)
            else:
                board[row][col] = 'B'
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        x = row + i
                        y = col + j
                        # out of boundary
                        if x < 0 or x >= m or y < 0 or y >= n:
                            continue
                        if board[x][y] == 'E': 
                            self.updateBoard(board, [x,y])
                
        return board  
         
        
        # optimize the code above
        # https://www.cnblogs.com/grandyang/p/6536694.html
        

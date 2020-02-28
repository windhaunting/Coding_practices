#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 23:56:15 2018

@author: fubao
"""

'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

'''

# analysis
'''
case 1: all four directions are arounded by X
X X X
X O X
X X X

X X X X
X O O X
X X X X

X X X X
X O O X
X X O X

X X X X
X O O X
X X X X
X O O X
X X O X

X X X X
X O O X
X X O X
X O X X

'''

#1st naive way:
#思路：如果直接从一个'O'开始搜索判断是不是会到达边界，将会非常麻烦，因为需要保存路径上的每个'O'，
#如果到达边界就放弃这片区域的所有值，否则将其变为'X'。

#2nd 有一种更为聪明的做法是从四个边界出发，用DFS算法将从边界开始的'O'的区域都变成另外一个临时的值，
#这样做完之后剩下的‘O’将会是被包围的，然后将其变为‘X’，再将临时的值变为'O'即可

#could use DFS recursive or BFS iterative way


#3rd  we could use union-find method to solve this question?
# 2nd  use DFS traverse from 4 directions of borders of board, similar to number of islands

def solve(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """

    if len(board) == 0:
        return 
    m = len(board)
    n = len(board[0])
    
    for i in range(0, m):
        if board[i][0] == 'O':
            DFS(board, i, 0)
    for i in range(0, m):
        if board[i][n-1] == 'O':
            DFS(board, i, n-1)
            
    for i in range(0, n):
        if board[0][i] == 'O':
            DFS(board, 0, i)

    for i in range(0, n):
        if board[m-1][i] == 'O':
            DFS(board, m-1, i)

    for i in range(0, m):
        for j in range(0, n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'Y':
                board[i][j] = 'O'
                
def DFS(board, i, j):
    if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j] != 'O':  
        return
    
    board[i][j] = 'Y'
    
    DFS(board, i+1, j)
    DFS(board, i-1, j)
    DFS(board, i, j-1)
    DFS(board, i, j+1)
   


#2nd method but use BFS iterative way

def solve2(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    m = len(board)    
    if m == 0:
        return 
    n = len(board[0])
    
    #border rows
    for i in range(0, m):
        bfs(board, i, 0)
        bfs(board, i, n-1)
        
    #border cols
    for j in range(0, n):
        bfs(board, 0, j)
        bfs(board, m-1, j)

    for i in range(0, m):
        for j in range(0, n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'Y':
                board[i][j] = 'O'
                
def bfs(board, i, j):
    if board[i][j] != 'O':
        return
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    qx = [i]     #row
    qy = [j]
    
    board[i][j] = 'Y'            # important to set 
    while(len(qx)):
        cx = qx.pop(0)
        cy = qy.pop(0)
        
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if nx >=0 and nx < len(board) and ny >= 0 and ny < len(board[0]) and board[nx][ny] == 'O':
                board[nx][ny] = 'Y'         #like record it's visited
                qx.append(nx)
                qy.append(ny)
    return
    
    
    
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solve2(board)

print (board)    
    
    
    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:07:02 2018

@author: fubao
"""

# 36. Valid Sudoku

'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

'''


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        l = 9
        m = 3
        row = [set([]) for i in range(0, l)]             #use set r hashtable
        col = [set([]) for i in range(0, l)]
        grid = [set([]) for i in range(0, l)]
        
        for r in range(0, l):
            for c in range(0, l):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
                    return False
                
                g = r/m*m + c/3
                if board[r][c] in grid[g]:
                    return False
                    
                grid[g].add(board[r][c])
                row[r].add(board[r][c])
                col[c].add(board[r][c])
        return True
        
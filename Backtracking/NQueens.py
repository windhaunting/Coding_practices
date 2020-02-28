#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 23:26:08 2018

@author: fubao
"""
# leetcode 51. N-Queens I, 52. N-Queens II



'''
 N-Queens I,

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.


Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' 
both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

output:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
 
'''


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        
        '''
        0 1 1 1
        1 0 1 1
        1 1 0 1
        1 1 1 1
        
        0 1 1 1
        1 1 1 0
        1 0 1 1
        1 1 1 1
        => 0 3, 1, 
        
        0 1 1 1
        1 1 0 1
        1 1 1 1
        1 1 1 1 
        
          #
         #
         #  #
         #  
        '''
        
        #1st use dfs backtracking
        
        def dfsHelper(nums, r, path, res):
            
            #base case , add a valid result
            if r == len(nums):
                #print ("solution: ", path)
                res.append(path)
                return 
            
            for c in range(len(nums)):    #place all colums one by one
                #check safe
                nums[r] = c
                if checkSafe(nums, r):        # check and prune
                    #M[r][col] = 1   #place queen in this position
                    tmp = "." *len(nums)
                    # recursive call 
                    dfsHelper(nums, r+1, path + [tmp[:c] + "Q" + tmp[c+1:]], res)
            
                    
                    
                    # go to next col
        def checkSafe(nums, r):
            '''
            check whether there is safe placing in that columns for the nth queen
            '''
            for i in range(r):
                if nums[i] == nums[r] or abs(nums[i] - nums[r]) == r-i:     # conflict in the same column, and diagonal  (i, i), (j, j)  check (i-j) = (i-j)
                    return False
            return True
        
        nums = [-1] * n
        res = []                                          
        dfsHelper(nums, 0, [], res)
        return res
                                                 
        '''
        O(n^n) is an upper bound on solving n-queens using backtracking.
        I'm assuming that solving this by assigning a queen column-wise.   
        However, consider this - when you assign a location of the queen in the first column, you have n options, after that, you only have n-1 options as         you can't the queen in the same row as the first queen, then n-2 and so on. Thus, the worst-case complexity is still upper bounded by O(n!).
        '''
        
 
'''
52. N-Queens II
         
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
'''

        
                
        def dfsHelper(nums, r):
            
            #base case , add a valid result
            if r == len(nums):
                self.count += 1
                #print ("solution: ", self.count)
                return 
            
            for c in range(len(nums)):    #place all colums one by one
                #check safe
                nums[r] = c
                if checkSafe(nums, r):        # check and prune
                    #M[r][col] = 1   #place queen in this position
                    tmp = "." *len(nums)
                    # recursive call 
                    dfsHelper(nums, r+1)
            
                    
        def checkSafe(nums, r):
            '''
            check whether there is safe placing in that columns for the nth queen
            '''
            for i in range(r):
                if nums[i] == nums[r] or abs(nums[i] - nums[r]) == r-i:     # conflict in the same column, and diagonal  (i, i), (j, j)  check (i-j) = (i-j)
                    return False
            return True
        
        nums = [-1] * n
        self.count = 0                                         
        dfsHelper(nums, 0)
        return self.count
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:03:11 2018

@author: fubao
"""


#

'''
We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is
 interpreted as a binary number, and the score of the matrix is
 the sum of these numbers.

Return the highest possible score.



Note:

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.

'''




def matrixScore(A):
    """
    :type A: List[List[int]]
    :rtype: int
    """
    
    #   e.g.


    '''
    Input: [[0,0,1,1],
            [1,0,1,0],
            [1,1,0,0]]
    Output: 39
    
    final output
    [[1,1,1,1],
     [1,0,0,1],
     [1,1,1,1]].
     
     
     I find maximizing the left-most digit is more important than any other digit.
     
     first move the first number as 1 for each row if it is 0
     we have:
         [1,1,0,0],
         [1,0,1,0],
         [1,1,0,0]
         
    Then we consider columns, if the column's most of them are 0, (use sum to consider this sum>w/2?)
    then toggle the column 
         [1,1,1,0],
         [1,0,0,0],
         [1,1,1,0]
    then 
     [1,1,1,1,
     [1,0,0,1],
     [1,1,1,1]
     
    '''


    if A is None or len(A) == 0:
            return 0
    
    l = len(A)
    w = len(A[0])
    
    #iterate rows here
    for i in range(0, l):
        if A[i][0] == 0:
            #toggle it
            for j in range(0, w):
                A[i][j] = 1 - A[i][j]
    #print ("A: ", A)
    
    # then consider the column
    
    #iterate rows here
    for j in range(1, w):
        s = 0        # sum 
        for i in range(0, l):
            s += A[i][j]
        if s < float(l)/2.0:   #toggle     double type
            for i in range(0, l):
                A[i][j] = 1 - A[i][j]
        
    #print ("A: ", A)
    
    ans = 0
    for j in range(0, w):
        for i in range(0, l):
            ans += 2**(w-j-1)*A[i][j]
    return ans

    
# same idea, but smarter and simpler python code

# reference :
    
# https://leetcode.com/problems/score-after-flipping-matrix/solution/

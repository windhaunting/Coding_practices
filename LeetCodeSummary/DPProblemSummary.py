#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 11:22:05 2018

@author: fubao
"""

#    Dp  summary



(1) identifying the DP problem
Typically, all the problems that require to maximize or minimize certain quantity or counting problems that
 say to count the arrangements under certain condition or certain probability problems can be solved by using Dynamic Programming.
All dynamic programming problems satisfy the overlapping subproblems property and most of the 
classic dynamic problems also satisfy the optimal substructure property. Once, we observe 
these properties in a given problem, be sure that it can be solved using DP.


note: 
    # if DFS recursive can work and it's max/min, number, boolean problem,
    # it could possibly be solved with DP

how to analyse:
    
    (1)initialize state
    (2)transition function
    (3) memoization
    
so we can use a one dimensional array or two dimensional array to start analye the problem

e.g.
  # Use at least one character before *.
#   p a b *
# s 1 0 0 0
# a 0 1 0 1
# b 0 0 1 1
# b 0 0 0 ?

                    
(2) categories of DP problem
# 1st  use one dimensional array when using DP
  probably the size is defined one bigger the original  input size

e.g.:
    
  Decode ways
    

# 2nd use two dimensional arrays when using DP
  probably the size is defined one bigger the original  input size
    
e.g.:
      
  regular expression Matching
    
    
  #note: some two dimensional array data structure could be reduced to one dimensional array
  
  
  examples:
      
      322. Coin Change
      
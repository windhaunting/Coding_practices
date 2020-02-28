#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 11:29:19 2018

@author: fubao
"""


#   graph problem       #google interview

'''
You are standing on the shore of a river.

You
----------------------------------------
|  |  |  |  |
O - O - O - O - O
|  |  |  |  |
O - O - O - O - O
|  |  |  |  |
O - O - O - O - O
|  |  |  |  |
O - O - O - O - O
|  |  |  |  |
----------------------------------------
You want to get here.

Questions:
- What is a good data structure to represent these islands and to use with the following functions?
    - is_connected(island_1, island_2) -- constant time
    - remove_bridge(island_1, island_2) -- constant time
    - make_storm()
    - can_get_to_other_shore()
- Can you please implement these functions.
- Bonus question:
    - If you start out with the river and bridges EXACTLY as shown above, and then call make_storm() and then call can_get_to_other_shore(), what is the chance, can_get_to_other_shore() returns True?

Assumptions:
-- No limitations on memory.
-- Adjacency matrix is already initialized with existing structure
-- Non-existent islands are never connected to any other island

'''

'''
Answers:
1. Use an adjacency matrix.  Islands and shores are nodes, and bridges are edges.  
Each node gets its own index and matrix entry (i, j) is 1 if there is a bridge directly connecting island i
to island j or 0 otherwise.

'''
# Question:  undirected  graph? 

def is_connected(A, island_1, island_2):
    if not A:
      return False
    M = len(A)           # nodes
    if island_1 >= M or island_2 >=M:
      return False
    if A[island_1][island_2] == 1:
        return True
    return False

A = [[1,1,1,1],
     [1,1,0,1],
     [1,0,1,0],
     [1,1,0,1]]

print (" is connected: ", is_connected(A, 3, 1))


def remove_bridge(A, island_1, island_2):
    if not A:
      return False
    M = len(A)
    if island_1 >= M or island_2 >=M:
      return False
    if A[island_1][island_2] == 1:
        A[island_1][island_2] = 0
        A[island_2][island_1] = 0
      

# storm break bridge
import random
def make_storm(A):
M = len(A)
T = [0 for i in range(M)] for j in range(M)]
for i in range(0, M):
    for j in range(0,M):
      if T[i][j] == 0:

      T[i][j] = 1

      T[j][i] = 1

      if A[i][j] == 1:

          #toss coin

          r = random.randint(0,1):

          if r == 1:

            A[i][j] == 0   
      
        
def can_get_to_other_shore(A):
  #get the node of the shore
    S1 = getShore1(A)
    S2 = getShore2(A)

    return DFS(S1,S2)

    def DFS(S1, S2):
        ls = []             # as a stack
        ls.append(S1)
        visited = [False] * len(A)
        visited[S1] = True
       
        while(len(ls)):
            t = ls.pop(-1)
            for n is in neighbor(t):
                if n == S2:
                    return True
                if not visited[n]:
                    ls.append(n)
                    visited[n] = True
        return False

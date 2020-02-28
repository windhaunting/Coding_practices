#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 14:54:14 2018

@author: fubao
"""

# Matrix related problem:


#Questions
# sparse matrix multiplicatin

# leetcode 542. 01 Matrix , nearest distance for each cell 1 to 0
# https://leetcode.com/problems/01-matrix/description/



'''
1. sparse matrix multiplication


Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.


A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
    (2, 3)   (3, 3)              
                  
'''
# https://www.programcreek.com/2014/10/leetcode-sparse-matrix-multiplication-java/


#1st naive method;  directly multiply by definition

def matrixMultiply1(A, B):
    # validation check
    
    # time complexity is O(Ar * Ac * Bc)
    Ar = len(A)
    Ac = len(A[0])
    
    Br = len(B)
    Bc = len(B[0])
    if Ac != Br:
        print ("Can not multiply")
    
    ans = [[0]*Bc for i in range(Ar)]
    for i in range(Ar):
        for j in range(Bc):
            for k in range(Ac):
                ans[i][j] += A[i][k] * B[k][j]
    return ans

A = [[1, 0, 0], [-1, 0, 3]]
B = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]

print (" ans: ", matrixMultiply1(A, B))



# one optimization, judge ifA[i][k] != 0 or B[k][j] != 0,  then we do the multiplication
# 首先遍历A数组，要确保A[i][k]不为0，才继续计算，然后我们遍历B矩阵的第k行，如果B[K][J]不为0
#我们累加结果矩阵res[i][j] += A[i][k] * B[k][j]; 这样我们就能高效的算出稀疏矩阵的乘法

def matrixMultiply2(A, B):
    # validation check
    
    # time complexity is O(Ar * Ac * Bc)
    Ar = len(A)
    Ac = len(A[0])
    
    Br = len(B)
    Bc = len(B[0])
    if Ac != Br:
        print ("Can not multiply")
    
    ans = [[0]*Bc for i in range(Ar)]
    for i in range(Ar):
        for k in range(Ac):
            if A[i][k] != 0:
                for j in range(Bc):
                    if B[k][j] != 0:
                        ans[i][j] += A[i][k] * B[k][j]
    return ans

A = [[1, 0, 0], [-1, 0, 3]]
B = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]

print ("2 ans: ", matrixMultiply2(A, B))


#3rd continue to optimize time with a bittle more space sacrified
'''
 方法其实核心思想跟上面那种方法相同，
稍有不同的是我们用一个二维矩阵矩阵来记录每一行中，
各个位置中不为0的列数和其对应的值，
然后我们遍历这个二维矩阵，取出每行中不为零的列数和值，然后遍历B中对应行进行累加相乘
'''

def matrixMultiply3(A, B):
    # validation check
    
    # time complexity is O(Ar * Ac * Bc)
    Ar = len(A)
    Ac = len(A[0])
    
    Br = len(B)
    Bc = len(B[0])
    if Ac != Br:
        print ("Can not multiply")
    storeNonZero = [[] for i in range(Ar)]   # for each line
    for i in range(Ar):
        for j in range(Bc):
            if A[i][j] != 0:
                storeNonZero[i].append((j, A[i][j]))
    
            
    ans = [[0]*Bc for i in range(Ar)]
    for i in range(Ar):
        for k in range(len(storeNonZero[i])):
            col = storeNonZero[i][k][0]
            val = storeNonZero[i][k][1]
            
            for j in range(Bc):
                ans[i][j] += val * B[col][j]

    return ans

A = [[1, 0, 0], [-1, 0, 3]]
B = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]

print ("3 ans: ", matrixMultiply3(A, B))
   





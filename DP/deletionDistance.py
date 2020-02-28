#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 23:49:28 2019

@author: fubao
"""


'''
Deletion Distance
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.

Examples:

input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0
'''



def deletion_distance(str1, str2):
  pass # your code goes here

  #idea 1 top-down method
  #fn(str1, str2) == 1 + min(fn(str1[1:], str2), fn(str1, str2[1:]))
   
  i = 0
  j = 0
  memo = {}
  res = helper(memo, str1, str2, i, j)

  print ("res: ", res)
  return res
def helper(memo, str1, str2, i, j):
  print ("i, j ", i, j)
  if i == len(str1):
    return len(str2)- j
  if j == len(str2):
    return len(str1) - i
  print ("i, j2222 ", i, j)
  if(i, j) in memo:
    return memo[(i,j)]
  print ("i, j3333 ", i, j, str1, str2)
  if str1[i] == str2[j]:    
    memo[(i+1, j+1)] = helper(memo, str1, str2, i+1, j+1)
    return memo[(i+1, j+1)]
  memo[(i+1,j+1)] = 1 + min(helper(memo, str1, str2, i+1, j), helper(memo, str1, str2, i, j+1))
  return memo[(i+1,j+1)]
  
assert deletion_distance("", "") == 0


    # 2 idea 2 bottom -up 
    for i in range(0, len(str1)+1):
        DP[i][0] = i
      
    for j in range(0, len(str2)+1):
        DP[0][j] = j
    
    if str[i] == str[j]: 
    # dog   frog =>  do  frog
    DP[i][j] =  DP[i-1][j-1]
    else:    
    #  dog   vs   froa   =>  dog vs fro    do  vs  froa;   do vs fro 2+ DP[i-1][j-1]
    DP[i][j] =  1+ min(DP[i][j-1], DP[i-1][j])
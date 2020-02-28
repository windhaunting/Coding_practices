#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 23:05:10 2018

@author: fubao
"""

# Leetcode edit distance similar questions:

'''

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. 
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

'''

'''

base case:

    DP[0][0] = 0
    DP[0][j] = j
    DP[i][0] = i


    function:

    i-1, j
    i, j-1
    
    if str1[i] != str2[j]
      DP[i][j]  = 1+min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1])
    else:
      DP[i][j] = DP[i-1][j-1]
    return DP[len(str1)][len(str2)]
    
time complexity o(m*n);
space complexity o(m*n)

'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        #pass # your code goes here

        l1 = len(word1)
        l2 = len(word2)

        DP = [[0]*(l2+1) for i in range(l1+1)]

        for i in range(0, l1+1):
            for j in range(0, l2+1):
                if i == 0:
                    DP[i][j] = j
                elif j == 0:
                    DP[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = 1 + min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1])

        return DP[l1][l2]
    
    
    

# Deletion Distance

'''

# Deletion Distance

The deletion distance of two strings is the minimum number of characters you need to delete in the two strings 
in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance 
between them. Explain how your function works, and analyze its time and space complexities.


'''




'''
  #hash map doesn't work for this case:
  "ab",  vs "ba"
  
  given two strs
  
  'd', vs 'e'
  
  "de", "ce"
  
  hash1 
  hash2 
  
  "dee", "dc"
  
  hash1: {d: 1, e:2}
  hash2: {d: 1, c: 1}
    
   m, n
   o(m+n)
    
    for d in hash1:
      if d in hash1 and d in h2
         count += difference of value
         delete d from h2
      
      elif d in h1:
          count+= h1[d]
          
    o(m)
    for d, val in hash2
        count += val
    o(n-m)
  
    o(m+n)
    o(m+n)

    ab,ba

    "ab", "ba"


    "a",  ""
    "a", "b"
    "a",  "a"
     "b",  "b"

    "ab", "ba"

    "ab", "cb"
    "ab", "ad"

    "", ""
    s1 = s2
    len(str1)+1)*(len)

    base case:

    DP[0][0] = 0
    DP[0][j] = j
    DP[i][0] = i


    function:

    i-1, j
    i, j-1
    
    if str1[i] != str2[j]
    
     DP[i][j]  = 1+   min(DP[i-1][j], DP[i][j-1])
    else:
      DP[i][j] = DP[i-1][j-1]
    return DP[len(str1)][len(str2)]
    
    
    "ab",  "ca"
         a  b 
       0 1  1
    c  1 2  3
    a  1 1  4
    
   
    "ab", "ca"

    o(m*n)
    
    '''
    
def deletion_distance(word1, word2):
    #pass # your code goes here
    
    l1 = len(word1)
    l2 = len(word2)

    DP = [[0]*(l2+1) for i in range(l1+1)]

    for i in range(0, l1+1):
        for j in range(0, l2+1):
            if i == 0:
                DP[i][j] = j
            elif j == 0:
                DP[i][j] = i
            elif word1[i-1] == word2[j-1]:
                DP[i][j] = DP[i-1][j-1]
            else:
                DP[i][j] = 1 + min(DP[i-1][j], DP[i][j-1])

    return DP[l1][l2]
    
'''
Solution 2 reduce space

The solution above takes O(N⋅M) space since we save all previous values, but notice that opt(i,j) requires only opt(i-1,j),
 opt(i,j-1) and opt(i-1,j-1). Thus, by iterating first through 0 ≤ i ≤ str1Len, and then for every i calculating 
 0 ≤ j ≤ str2Len, we need only to save the values for the current i and the last i. This will reduce the space needed for the function.

Pseudocode:

function deletionDistance(str1, str2):
    # make sure the length of str2 isn't
    # longer than the length of str1
    if (str1.length < str2.length)
        tmpStr = str1
        str1 = str2
        str2 = tmpStr

    str1Len = str1.length
    str2Len = str2.length
    prevMemo = new Array(str2Len  + 1)
    currMemo = new Array(str2Len  + 1)

    for i from 0 to str1Len:
        for j from 0 to str2Len:
            if (i == 0):
                currMemo[j] = j
            else if (j == 0):
                currMemo[j] = i
            else if (str1[i-1] == str2[j-1]):
                currMemo[j] = prevMemo[j-1]
            else:
                currMemo[j] = 1 + min(prevMemo[j], currMemo[j-1])

        prevMemo = currMemo
        currMemo = new Array(str2Len + 1);  
                                           
    return prevMemo[str2Len]
Time Complexity: the time complexity stays the same, i.e. O(N⋅M), since we still run a nested loop with N⋅M iterations.

Space Complexity: O(min(N,M)), as we only need to hold two rows of the double array.
'''

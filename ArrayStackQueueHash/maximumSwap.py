#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 09:37:47 2018

@author: fubao
"""


'''
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
'''


def maximumSwap(self, num):
    """
    :type num: int
    :rtype: int
    """
    #1st naive way is to sort the number first, get a new number-newNum
    #then compare each element between the num and newNum from left to right; special case: multiple biggest number, consider the rightmost one
    
    '''
    #SUCCESS 2nd way is to iterate elements from left to right, and find the element a on its right that is biggest than the element b by searching from right to left. if there is bigger element than the element a then swap       #e.g. 2736 -> 7236  find the maximum 7;   2367->7362...
    
    stNum = str(num)
    for i in range(0, len(stNum)):
        maxNum = stNum[i]
        maxPos = i
        j = len(stNum)-1
        while(j >=i):
            if stNum[j] > maxNum:          # if two or more are biggest;  2737   ; but 98368
                maxNum = stNum[j]
                maxPos = j
            j -= 1
        #print ("maxPos: ", maxPos, i, j)

        if maxPos != i:
            #swap 
            newNum = int(stNum[0:i] + stNum[maxPos] + stNum[i+1:maxPos] + stNum[i] + stNum[maxPos+1:])
            #print ("newNum: ", newNum, maxPos, i)
            return newNum
    return num
    '''
        
    #SUCCESS 3rd way; use a bucket;  0--9 digits;  get the the last index of digits in Num and put into a bucket according to its index; 
    stNum = str(num)
    bucket = [-1] * 10
    for i, sn in enumerate(stNum):       # get bucket num
        bucket[int(sn)] = i
    #print ("bucket: ", bucket)
    for i in range(0, len(stNum)):
        for j in range(len(bucket)-1, int(stNum[i]), -1):
            #print ("j: ", j, i)
            if bucket[j] > i:
                #swap 
                newNum = int(stNum[0:i] + stNum[bucket[j]] + stNum[i+1:bucket[j]] + stNum[i] + stNum[bucket[j]+1:])
                #print ("newNum: ", newNum, maxPos, i)
                return newNum
    
    return num

        
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:16:17 2018

@author: fubao
"""


# Random return number according to weight


'''
Given n numbers, each with some frequency of occurrence. Return a random number with probability proportional to its frequency of occurrence.

Example:

Let following be the given numbers.
  arr[] = {10, 30, 20, 40}  

Let following be the frequencies of given numbers.
  freq[] = {1, 6, 2, 1}  

The output should be
  10 with probability 1/10
  30 with probability 6/10
  20 with probability 2/10
  40 with probability 1/10 
  

'''

#  https://www.geeksforgeeks.org/random-number-generator-in-arbitrary-probability-distribution-fashion/

# 1st idea is to copy item's each frequency times and put into the element of arr, and then randomly generated list from arr,
# that take much memory

# 2nd : generate a pre-sum of weights, and then get the total sum weights[-1], then randomly generate a number k from the (0, weights[-1]), then search 
#from weigths to find it closest index ind, draw arr[ind] from arr, in this way, each arr would have equally likely range

import random
def randomGenerateWeight(arr, freq):
    
    # pre-sum freq
    for i in range(1, len(freq)):
        freq[i] += freq[i-1]
    
    #get range of weights
    maxSum = freq[-1]
    
    randNum = random.randrange(0, maxSum)       
    ind = binarySearch(freq, randNum)
    
    return arr[ind]

def binarySearch(freq, target):
    
    left = 0
    right = len(freq)-1
    while (left <= right):
        mid = int(left + (right-left)/2)
        
        if freq[mid] == target:
            return mid
        elif freq[mid] < target:
            left = mid+1
        else:
            right = mid - 1
    return left


arr = [3, 4, 5, 1]
freq = [1,3, 8, 2]
randNum = randomGenerateWeight(arr, freq)
print ("randNum: ", randNum)

'''
case 1:  [1, 4, 12, 14]



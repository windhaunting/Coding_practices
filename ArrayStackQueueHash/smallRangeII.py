#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 10:08:11 2018

@author: fubao
"""


# 910. Smallest Range II


'''
Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

 

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
Example 3:

Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]
 

Note:

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
'''


class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        '''
        #1st method; how to know fast that use x=k or x=-k for each A[i];
        # is the rule that: if A[i] < k, we add A[i] + k; if A[i] > k; we do A[i] +k ?
        minVal = 2**32
        maxVal = -2**32
        B = []
        
        #test:
        for i, v in enumerate(A):
            x = i
            print ("i: ", i, v)
            if v <= K:
                tmp = v+K
            else:
                tmp = v-K
                
            if tmp < minVal:
                minVal = tmp

            if tmp > maxVal:
                maxVal = tmp
            B.append(tmp)
        #print ("min, max: ", minVal, maxVal, B)
        
        return maxVal - minVal
        '''
        
        
        #2nd method naive way would try all possible combinations of x+k or x-k for each A[i]; the total number of combination is 
        # 2^n ;  n = len(A)
        #of course, we need to consider an elegant way to improve this which increase +k, which decrease k; if we sort A; find the decison line of index to determine +k or -k ?
        
        # ref: https://leetcode.com/problems/smallest-range-ii/solution/
        #??  how to decide how many elements +k, how many elements -k; we have to try 
        A.sort()
        minVal = A[0]+K
        maxVal = A[-1]-K
        res = A[-1]-A[0]
        
        for i in range(0, len(A)-1):
            l = A[i]
            r = A[i+1]
            low = min(minVal, r-K)     # minVal, maxVal, r-k, l+K
            high = max(l+K, maxVal)
            res = min(res, high-low)
        
        
        return res
        
        
        
        

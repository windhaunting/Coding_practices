#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 16:08:11 2018

@author: fubao
"""



#  334. Increasing Triplet Subsequence

'''
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.


'''


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
       #1st use DP idea;    similar to question longest increasing squence.
       # DP[i] indicate the number of increasing sequence before index i;
       # DP[i] = max(DP[i], DP[j] + 1)  ;  i = 1 to len(nums), if nums[j] < nums[i], j = 0 to i 
       #2nd more optimized approach
       # Start with the maximum numbers for the first and second element. Then:
       #(1) Find the first smallest number in the 3 subsequence
       #(2) Find the second one greater than the first element, reset the first one if it’s smaller

       #use O(n) time O(1) space
         # e.g. [1,5,1,2,3]
        #       [1,2,1,4,1]
        # [8, 7, 1, 2, 3]
        # [1, 5, 7, 2]
        #[2, 5, 1, 2 ]
        #define a minval and maxvalue, update the minvalue for the first non-ascending order 
        if nums is None or len(nums) == 0:
            return False
       
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
    
        #keep track the real sequence; dont work so far for this e.g. [5,1,5,5,0,0,0,0,8]
        '''
        first = second = secondMin = float('inf')
        for n in nums:
            if n <= first:
                if second < float('inf'):
                    secondMin = first
                first = n                
            elif n <= second:
                second = n
            else:
                secondMin = first if secondMin == float('inf') else secondMin
                print "first: {}, second: {}, third: {}".format(secondMin, second, n)
                return True
        return False
        '''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:27:10 2018

@author: fubao
"""



#  152. Maximum Product Subarray


'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.


'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        #1 brute force  time O(n2),     time limited
        maxV = -2**31
        for i in range(1, len(nums)+1):
            for j in range(0, len(nums)-i+1):
                tmp = 1
                k = 0
                while(k < i):
                    tmp *= nums[j + k]
                    k += 1
                maxV = max(tmp, maxV)
        return maxV
        '''
        
        #2nd DP method   
       # Maximum Subarray那题的变种。由于正负得负，负负得正的关系。以A[i]结尾的max product subarray同时取决于以A[i-1]结尾的max / min product subarray以及          #  A[i]本身。因此，对每个i，需要记录min/max product两个状态：
        
       #    maxP[i] = max(maxP[i-1]*nums[i], minP[i-1]*nums[i], nums[i])
       #    minP[i] = min(maxP[i-1]*nums[i], minP[i-1]*nums[i], nums[i])
        if len(nums) == 0:
            return 0
            
        maxCur = nums[0]
        minCur = nums[0]
        ret = maxCur
        for i in range(1, len(nums)):
            tmp = maxCur
            maxCur = max(maxCur * nums[i], minCur * nums[i], nums[i])
            minCur = min(tmp * nums[i], minCur * nums[i], nums[i])
            
            ret = max(maxCur, ret)
        return ret
        

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 00:11:59 2018

@author: fubao
"""




'''
238. Product of Array Except Self


Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

'''



class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #without division and o(n)
        # 
        
        # 1   1   2  6
        # 24  12  4  1 
        #return 24 12 8 6
        
        if len(nums) == 0 or nums is None:
            return []
        
        s = [1] * len(nums)
        for i in range(1, len(nums)+1):
            s[i] *= s[i-1] * nums[i]
        
        for i in range(len(nums)-2, -1, -1):
            
            
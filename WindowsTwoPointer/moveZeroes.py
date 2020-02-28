#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 15:36:39 2018

@author: fubao
"""



#   283. Move Zeroes


'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.


'''

# [0, 1, 0, 3, 12]
# i, j 
#  
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return 
        i = 0
        j = 1
        while ( j < len(nums)):
            if nums[i] != 0:
                #increase
                i += 1
                j += 1
            elif (nums[i] == 0) and (nums[j] !=0):
            #exchange
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j += 1
                
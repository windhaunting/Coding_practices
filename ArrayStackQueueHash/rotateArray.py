#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:32:19 2018

@author: fubao
"""





# 189. Rotate Array

'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?
Related problem: Reverse Words in a String II

'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #first method shift brute force:
        # I think time limit exceeded
        
        '''
        #second method: copy
        if k > len(nums): k = k%len(nums) 
        if k == 0:
            return
        nums[:] = nums[-k:] + nums[:(len(nums)-k)]
        '''
        
        '''
        #third method, recursive
        if k > len(nums): k = k%len(nums)
        if k == 0:
            return
        self.reverse(nums, 0, len(nums)-k-1)
        self.reverse(nums, len(nums)-k, len(nums)-1)
        self.reverse(nums, 0, len(nums)-1)
        '''
        #fourth method:
        #copy another array
        a = []
        for i in range(0, len(nums)):
            a.insert((i + k)%len(nums) ,nums[i])
        
        nums[:] = a[:]
        
    def reverse(self, nums, l, r):
        while (l < r):
            #exchange
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l += 1
            r -= 1
        
                
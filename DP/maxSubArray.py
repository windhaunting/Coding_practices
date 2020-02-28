#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 19:04:38 2018

@author: fubao
"""



# 53. Maximum Subarray that have the largest sum


'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [-2,1,-3,4,-1,2,1,-5,4]
        # [4,-1,2,1]
        
        #dp, maxRes[i] = max(maxRes[i-1] + nums[i], nums[i])       # it means if maxRes[i-1] < 0 ; not add to nums[i]
        #maxVal = max(maxRes[i], maxVal)
        
        '''
        if nums is None:
            return []
        maxRes = [0 for i in range(0,len(nums))]
        maxVal = nums[0]
        maxRes[0] = nums[0]
        for i in range(1, len(nums)):
            maxRes[i] = max(maxRes[i-1] + nums[i], nums[i])
            maxVal = max(maxRes[i], maxVal)
            
        return maxVal
        '''
        
        
        
        #USE Divde and Conquer approach
        def maxCrossSum(nums, l, m, h):
            lsum = -1 * sys.maxsize
            summ = 0
            for i in range(m, l-1, -1):
                summ += nums[i]
                if summ > lsum:
                    lsum = summ
            summ = 0
            rsum = -1 * sys.maxsize
            for i in range(m+1, h+1):
                summ += nums[i]
                if (summ > rsum):
                    rsum = summ
            return lsum + rsum
                
        def maxSubArraySum(nums, l, h):
            if l == h:
                return nums[l]
            m = (l + h)/2
            return max(maxSubArraySum(nums, l, m), maxSubArraySum(nums, m+1, h), maxCrossSum(nums, l, m, h))
        
        
        if nums is None:
            return []
        l = 0
        h = len(nums)
        return maxSubArraySum(nums, l, h-1)
        

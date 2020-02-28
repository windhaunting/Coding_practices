#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 19:20:19 2018

@author: fubao
"""




#  Maximum Size Subarray Sum Equals k
'''
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?


'''


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # reference:  http://www.cnblogs.com/grandyang/p/5336668.html
        
        
        # 我们就从题目中给的例子进行分析：
        '''
        nums: [1, -1, 5, -2, 3], k = 3
        
        sums: [1, 0, 5, 3, 6]
        
        我们可以看到累积和的第四个数字为3，和k相同，则说明前四个数字就是符合题意的一个子数组，再来看第二个例子：
        
        nums: [-2, -1, 2, 1], k = 1
        
        sums: [-2, -3, -1, 0]
        
        我们发现累积和中没有数字等于k，但是我们知道这个例子的答案是[-1, 2]，那么我们看累积和数组的第一和第三个数字，我们是否能看出一些规律呢，没错，第三个数字-1减去k，得到第一个数字，这就是规律，这也是累积和求区间和的方法，
        
        '''   
        
        # better way   O(n) time
        sum2pos = {0:0}
        ans = None
        tsum = 0
        for i in range(len(nums)):
            tsum += nums[i]
            wanted = tsum - k
            if wanted in sum2pos:
                length = i + 1 - sum2pos[wanted]
                if ans is None or length > ans:
                    ans = length
            if tsum not in sum2pos:
                sum2pos[tsum] = i + 1
        return ans or 0
    
    
    
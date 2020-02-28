#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 21:35:42 2018

@author: fubao
"""




# 45. Jump Game II


'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.

'''


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # greedy algorithm 
        
        '''
        The basic thoughts underline is a greedy style. Every one more jump, you want to jump as far as possible.
        In Jump Game I, when you at position i, you care about what is the furthest position could be reached from i th position. but here in Jump Game II, instead you care about what would be the next furthest jump could be made when you could reach as far as ith position from last jump.
     So you iterate all positions could be reached from last jump till i th position to find it out.
        '''
        jumps = curEnd = curFarthest = 0
        for i in range(len(nums) - 1):
            curFarthest = max(curFarthest, i + nums[i])
            if i == curEnd:
                jumps += 1
                curEnd = curFarthest
        return jumps
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:32:27 2018

@author: fubao
"""

# 78. Subsets
# powerset

#facebook

'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #SUCCESS;     first method
        # aggregate subset method like this
        '''     
        起始subset集为：[]
        添加S0后为：[], [S0]
        添加S1后为：[], [S0], [S1], [S0, S1]
        添加S2后为：[], [S0], [S1], [S0, S1], [S2], [S0, S2], [S1, S2], [S0, S1, S2]
        红色subset为每次新增的。显然规律为添加Si后，新增的subset为克隆现有的所有subset，并在它们后面都加上Si。
        '''
        '''
        res = [[]]
        nums.sort()
        for num in nums:
            res += [r + [num] for r in res]
            #print ('res ', res)
        return res
        '''
        
        '''
        #2nd use backtracking method
        #
        def dfs(depth, start, valLst):
            if valLst not in res:
                res.append(valLst)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth+1, i+1, valLst + [nums[i]])
        nums.sort()
        res = []
        dfs(0,0,[])
        return res
        '''
        
        #using bit operation
        #there ar 2^m -1 choices of subsets, m = len(nums)
        m = len(nums)
        lsts = []
        nums.sort()
        for i in range(0, 1 << m):
            tmp = []
            j = 0
            while (i):
                if i & 1:
                    tmp.append(nums[j])
                i = i >> 1
                j += 1
            if tmp not in lsts:
                lsts.append(tmp)
        return lsts
        
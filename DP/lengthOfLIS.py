#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 19:14:02 2018

@author: fubao
"""

# 300. Longest Increasing Subsequence facebook


'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?



'''

#naive o(2^n) generate all subsequence with length from 1 to n

# 2nd use DP ; O(N^2)
# reference http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-300-longest-increasing-subsequence/


#also BFS search method;   O(nlogn)

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        #1. naive method; time complexity o(n^2).   two layers iteration. 1) first iterate each element nums[i] in the nums, ,  2) second iteration to find the bigger num[j] to add as each list 3) then find the maximum length list in the lists. length[i] += 1 if nums[j] > nums[i]
        #or reversely, smaller nums[j] to update length[i].   i to 0 to len(nums), j = 0 to i; so length[i] = max(length[i], length[j]+1)
        
        '''
        #2n d use binary search, try to select and insert into the increasing sequence 
        #(1) maintain a result list ans = [nums[0]]
        #(2) iterate nums from second element num, compare num with the last element of ans: 
        #    a. if num < ans[-1]
        #           insert num into ans
        #      else  binary search in the ans the left insertion position for num (i.e. the smallest number that is bigger than num), and replace it
               
            
        def binarySearch(lst, ele):
            if len(lst) == 1:
                return 0
            l = 0
            h = len(lst) - 1
            while (l <= h):
                mid = (l+h)/2
                if lst[mid] == ele:
                    return mid
                elif lst[mid] < ele:
                    l = mid + 1
                else:
                    h = mid - 1
            if l >= len(lst):
                return -1
            return l
        
        if len(nums) == 0:
            return 0
        ansLst = []
        ansLst.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] > ansLst[-1]:
                ansLst.append(nums[i])
            else:
                #binary search
                pos = binarySearch(ansLst, nums[i])
                #print ('pos: ', len(ansLst), pos)
                ansLst[pos] = nums[i]
        return len(ansLst)
        '''
        
        #note it is for length of longest increasing sequence, the final ansLst may not be the real longest increasing sequence
        
        
    
        #3rd use Dynamic programming
        #use DP[i] indicate the length of longest increasing sequence at position i so far.
        #it has optimal substructure: every sublist has the optimal solution for the longest increasing sequence
        #overlapping subproblem: the large sublist problem is affected by the previous smaller sublist :
        #the transition equation:   DP[i] = max(DP[i], DP[j] + 1)  ;  if nums[j] < nums[i], i = 1 to len(nums),  j = 0 to i
        #intialize all DP element as 1
        if len(nums) == 0:
            return 0
        
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
        
        
        
        


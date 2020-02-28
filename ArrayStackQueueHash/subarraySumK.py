#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 22:18:32 2019

@author: fubao
"""

# facebook 560. Subarray Sum Equals K

'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        #TLE idea 1 naive method, which use traverse all the possible subarray of all the length, if find one, add to count += 1 then continue the second loop from the second index
        # take O(n^2) time 
        #consider 0 and -1 +1 
        
        res_cnt = 0
        cursum = 0
        for i in range(0, len(nums)):
            if nums[i] == k:
                res_cnt += 1
            
            cursum = nums[i]
            for j in range(i+1, len(nums)):
                cursum += nums[j]
                if cursum == k:
                    res_cnt += 1
                    
                    
                    
        return res_cnt
        '''

        '''
        #failure idea 2 try o(n) failure without consider negative value how to optimize, stop early if the value is more than K, maintain the current currsum,  and the starting index i and current index j
        
        
        i = 0
        res_cnt = 0
        start_ind = 0
        end_ind = 0
        cursum = 0
        
        
        for n in nums:
            if n == k:
                res_cnt += 1
                
        while (i < len(nums)):
            end_ind = i
            if cursum < k:
                cursum += nums[i]
                if cursum == k and (end_ind - start_ind) > 0:
                    res_cnt += 1
                    cursum -= nums[start_ind]
                    start_ind +=1
            else:
                cursum -= nums[start_ind]
                #print("cursum222333: ", cursum, start_ind)
                start_ind += 1
            #print ("cursum: ", cursum, res_cnt)
            i += 1
            
        return res_cnt
    
        '''
       
    
        # reference online https://www.geeksforgeeks.org/number-subarrays-sum-exactly-equal-k/
        #here prefix has [0, num[0], num[0] + num[1], ...]
        #prefixsum[j] - prefixsum[i] = sum(num[i:j]) = k
        # therefore, prefixsum[i] = prefixsum[j] - k, if exist a value in the prefix, then we must have found a subarray which satisfying the condition 
        
        #default return 0, no need to write corner cases?
        
        dic_presum_cnt = {0:1}

        res = 0
        presum = 0
        for i in range(0, len(nums)):
            presum += nums[i]

            extra = presum - k
            if extra in dic_presum_cnt:
                res += dic_presum_cnt[extra]
                
            if presum not in dic_presum_cnt:
                dic_presum_cnt[presum] = 1
            else:
                dic_presum_cnt[presum] += 1

        return res
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                
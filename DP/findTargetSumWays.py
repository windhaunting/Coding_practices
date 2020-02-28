#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 00:33:28 2018

@author: fubao
"""



#  494. Target Sum

'''
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

'''

#  reference :  https://leetcode.com/problems/target-sum/discuss/97335


class Solution(object):
    count = 0
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        
        
        
        
  #1st 1. 1st use  DFS recursive,  like a binary tree;   Go to left (+1) or right (-1); then  when sum is S  go the upper next
        #Time complexity : O(2^n)   Size of recursion tree will be 2^n.   n refers to the size of numsnums array.

        #Space complexity : O(n)O(n). The depth of the recursion tree can go upto n.     
        #TLE for python
        
        def findTargetHelper(nums, index, sumNum):
            if index == len(nums):
                if sumNum == S:
                    self.count = self.count + 1
                return
             
        
            findTargetHelper(nums, index+1, sumNum - nums[index])         #+1
            findTargetHelper(nums, index+1, sumNum + nums[index])         #-1
        
        findTargetHelper(nums, 0, 0)

        return self.count
    
    
    
    #2 Use DP
    #  reference: https://leetcode.com/problems/target-sum/solution/
   #use dp[i][j] to define the number of assignment that lead to sum j up to the ith index 
   #dp[i][sum+num[i]] = dp[i][sum+num[i]] + dp[i-1][sum] 
   #dp[i][sum-num[i]] = dp[i][sum-num[i]] +dp[i-1][sum]
   
   
      '''
        #2nd DP
        
        #    dp[i][sum+num[i]] = dp[i][sum+num[i]] + dp[i-1][sum] 
        #    dp[i][sum-num[i]] = dp[i][sum-num[i]] +dp[i-1][sum]
    
        sumN = sum(nums)
        if sumN < S or (sumN+S)%2 != 0:
            return 0
        
        #initialize
        dp = [[0]*(2*sumN+1) for i in range(0, len(nums))]
        dp[0][nums[0] + sumN] = 1
        dp[0][-1*nums[0] + sumN] +=1
        
        #iterate for dp
        for i in range(1, len(nums)):
            for s in range(-1*sumN, sumN+1, 1):
                
                if dp[i-1][s+sumN] > 0:
                    print ("tb: ", i, s+sumN+nums[i], dp[i-1][s + sumN], dp[i][s + sumN + nums[i]])

                    dp[i][s + sumN + nums[i]] += dp[i-1][s + sumN]
                    dp[i][s + sumN - nums[i]] += dp[i-1][s + sumN]
                    print ("t: ", i, s+sumN+nums[i], dp[i-1][s + sumN], dp[i][s + sumN + nums[i]])
                    print ("y: ", i, s+sumN+nums[i], dp[i-1][s + sumN], dp[i][s + sumN - nums[i]])
                    
        return dp[len(nums)-1][S + sumN]
    
        '''


        # 3rd
        '''
        We can observe that for the evaluation of the current row of dpdp, only the values of the last row of dp are needed. Thus, we can save some   space by using a 1D DP array instead of a 2-D DP array. The only difference that needs to be made is that now the same dpdp array will be updated for every row traversed.
        '''
        
        sumN = sum(nums)
        if sumN < S or (sumN+S)%2 != 0:
            return 0
        
        #initialize
        dp = [0] * (2*sumN+1)
        dp[nums[0] + sumN] = 1
        dp[-1*nums[0] + sumN] +=1
        
        #iterate for dp
        for i in range(1, len(nums)):
            tmp = [0] * (2*sumN+1)
            for s in range(-1*sumN, sumN+1, 1):
                if dp[s+sumN] > 0:
                    tmp[s + sumN + nums[i]] += dp[s + sumN]
                    tmp[s + sumN - nums[i]] += dp[s + sumN]
                    
                    #print ("t: ", i, s+sumN+nums[i], dp[i-1][s + sumN], dp[i][s + sumN + nums[i]])
                    #print ("y: ", i, s+sumN+nums[i], dp[i-1][s + sumN], dp[i][s + sumN - nums[i]])
            dp = tmp
        
        
        return dp[S + sumN]
    


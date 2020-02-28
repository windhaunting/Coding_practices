#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 00:43:26 2018

@author: fubao
"""


# combinationSum IV 

'''
 Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.                

'''

'''

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

'''

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
         
    # use DP 
    # So we know that target is the sum of numbers in the array. 
    #Imagine we only need one more number to reach target, this number can be any one in the array, right? So the # of combinations of target
    
    #dp[i] indicate the number of possible combinations with sum = i
    # dp[target] = sum(dp[target - nums[i]]) for i from 0 to len(nums)-1 and target > nums[i]



# 1st java recusive
'''

public int combinationSum4(int[] nums, int target) {
    if (target == 0) {
        return 1;
    }
    int res = 0;
    for (int i = 0; i < nums.length; i++) {
        if (target >= nums[i]) {
            res += combinationSum4(nums, target - nums[i]);
        }
    }
    return res;
}
   
     
#2nd DP 
        
Now for a DP solution, we just need to figure out a way to store the intermediate results, 
to avoid the same combination sum being calculated many times.
 We can use an array to save those results, and check if there is already a result before calculation. 
 We can fill the array with -1 to indicate that the result hasn’t been calculated yet. 0 is not a 
 good choice because it means there is no combination sum for the target.

private int[] dp;

public int combinationSum4(int[] nums, int target) {
    dp = new int[target + 1];
    Arrays.fill(dp, -1);
    dp[0] = 1;
    return helper(nums, target);
}

private int helper(int[] nums, int target) {
    if (dp[target] != -1) {
        return dp[target];
    }
    int res = 0;
    for (int i = 0; i < nums.length; i++) {
        if (target >= nums[i]) {
            res += helper(nums, target - nums[i]);
        }
    }
    dp[target] = res;
    return res;
}
EDIT: The above solution is top-down. How about a bottom-up one?

public int combinationSum4(int[] nums, int target) {
    int[] comb = new int[target + 1];
    comb[0] = 1;
    for (int i = 1; i < comb.length; i++) {
        for (int j = 0; j < nums.length; j++) {
            if (i - nums[j] >= 0) {
                comb[i] += comb[i - nums[j]];
            }
        }
    }
    return comb[target];
}
            
'''
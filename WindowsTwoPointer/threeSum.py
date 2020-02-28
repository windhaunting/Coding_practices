ytho#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:13:36 2018

@author: fubao
"""



# 15. 3Sum   3 sum three sum


'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''


#1st   use hashmap and 2 sum idea

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        #one idea using the 2sum method, using hash
        target = 0     #target = 0 here
        
        if not nums:
            return []
        resLst = []
        #nums.sort()
        for i in range(0, len(nums)):
            d1 = target - nums[i]
            
            indMap = {}
            #using 2 sum to get d1
            
            for j in range(i+1, len(nums)):
                d2 = d1 - nums[j]
                if d2 in indMap:
                    innerLst = []
                    innerLst.append(nums[i])
                    innerLst.append(nums[j])
                    innerLst.append(d2)
                    innerLst.sort()
                    if innerLst not in resLst:
                        resLst.append(innerLst)

                else:
                    indMap[nums[j]] = j
        return resLst
    
    
# 2nd use sort and binary search
'''
The idea is to sort an input array and then run through all indices of a possible first element of a triplet. 
For each possible first element we make a standard bi-directional 2Sum sweep of the remaining part of the array.
 Also we want to skip equal elements to avoid duplicates in the answer without making a set or smth like that.
'''

# Java code
public List<List<Integer>> threeSum(int[] num) {
    Arrays.sort(num);
    List<List<Integer>> res = new LinkedList<>(); 
    for (int i = 0; i < num.length-2; i++) {
        if (i == 0 || (i > 0 && num[i] != num[i-1])) {
            int lo = i+1, hi = num.length-1, sum = 0 - num[i];
            while (lo < hi) {
                if (num[lo] + num[hi] == sum) {
                    res.add(Arrays.asList(num[i], num[lo], num[hi]));
                    while (lo < hi && num[lo] == num[lo+1]) lo++;
                    while (lo < hi && num[hi] == num[hi-1]) hi--;
                    lo++; hi--;
                } else if (num[lo] + num[hi] < sum) lo++;
                else hi--;
           }
        }
    }
    return res;
}
                
                

        
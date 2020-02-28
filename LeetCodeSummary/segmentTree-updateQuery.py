#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 18:35:56 2019

@author: fubao
"""

# build segment tree
# update
# sum Range Query



#segment tree code 1: use an array to store tree


# 

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sumLst = [0]*(len(nums)*3)    # use the array to represent the tree
        
        if not nums or len(nums) == 0:
            return
        self.createSegTree(nums)      # create tree
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        l = 0
        r = len(self.nums)-1
        self.updateSumLst(i, val, l, r, 0)
        
    def  updateSumLst(self, i, val, l, r, nd_ind):
    
        if l == r:
            self.nums[i] = val
            self.sumLst[nd_ind] = val
        else: 
            mid = l + (r-l)/2

            left_ind = 2*nd_ind + 1
            right_ind = 2*nd_ind +2
            if i >= l and i <= mid:  # go to left
                self.updateSumLst(i, val, l, mid, left_ind)
            else:
                self.updateSumLst(i, val, mid+1, r, right_ind)

            self.sumLst[nd_ind] = self.sumLst[left_ind] + self.sumLst[right_ind]
        
            
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        l = 0
        r = len(self.nums)-1
        return self.sumRangeHelper(l, r, 0, i, j)
        
    def sumRangeHelper(self, l, r, nd_ind, i, j):
        # check i and j
        if r < i or j < l:
            return 0
        
        #if l == r:
        #    return self.sumLst[nd_ind]
        if i <= l and r <=j:              # find the range
            #print("ssse: ", l, r,nd_ind,self.sumLst[nd_ind])
            return self.sumLst[nd_ind]
        mid = l + (r-l)/2
        
        left_ind = 2*nd_ind + 1
        right_ind = 2*nd_ind +2
        
        sum_left = self.sumRangeHelper(l, mid, left_ind, i, j)
        sum_right = self.sumRangeHelper(mid+1, r, right_ind, i, j)
        return sum_left + sum_right
    
        
    def createSegTree(self, nums):
        l = 0
        r = len(nums)-1
        
        self.createSegTreeHelper(nums, l, r, 0, self.sumLst)
        #print("sumLst: ", self.sumLst)
        #return sumLst
    
    # build segment tree
    # https://www.youtube.com/watch?v=e_bK-dgPvfM
    def createSegTreeHelper(self, nums, l, r, nd_ind, sumLst):
        
        if l == r:
            sumLst[nd_ind] = nums[l]
        
        else:
            mid = l + (r-l)/2

            left_ind = 2*nd_ind + 1
            right_ind = 2*nd_ind + 2

            self.createSegTreeHelper(nums, l, mid, left_ind, sumLst)
            self.createSegTreeHelper(nums, mid+1, r, right_ind, sumLst)

            sumLst[nd_ind] = sumLst[left_ind] + sumLst[right_ind]

    


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)




# 2nd use pointer Tree structure  to store tree
            
# reference code:
https://www.programcreek.com/2014/04/leetcode-range-sum-query-mutable-java/
           
            
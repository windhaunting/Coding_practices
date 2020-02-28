#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:22:01 2018

@author: fubao
"""




#  Search in Rotated Sorted Array II

'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.

'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        # [1 1 1 1 1 1]  [1,1,1, 2,3,1]
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if target==nums[mid]:
                return True
            if nums[lo] == nums[mid] and nums[mid] == nums[hi]:
                lo += 1
                hi -= 1
            elif nums[lo] <= nums[mid]:
                if nums[lo]<=target<nums[mid]:
                    hi = mid -1
                else:
                    lo = mid + 1
            else:
                if nums[mid]<target<=nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 18:35:06 2018

@author: fubao
"""

#34. Search for a Range


'''

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        #method 1:  o(n) time complexity
        if not nums:
            return [-1,-1]
        resLst = []
        for i, n in enumerate(nums):
            if target == n:
                resLst.append(i)
            if n > target:
                break
        if len(resLst) == 0:
            return [-1, -1]
        elif len(resLst) == 1:
            return [resLst[0], resLst[0]]
        else:
           return [resLst[0], resLst[-1]]
        
        '''
        
        #method 2: o(logn)  binary search but worst case still o(n)
        if not nums:
            return [-1,-1]
        start = 0
        end = len(nums)-1
        resLst = []

        while (start <= end):
            mid= start + (end - start)/2
            if target == nums[mid]:
                resLst.append(mid)
                #print ("mid ...", mid)
                i = mid-1
                while (i >= 0):
                    if nums[i] == target:
                        resLst.insert(0, i)
                    else:
                        break
                    i -= 1
                i = mid+1
                while (i < len(nums)):
                    if nums[i] == target:
                        resLst.append(i)
                    else:
                        break
                    i += 1
                break
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        if len(resLst) == 0:
            return [-1, -1]
        elif len(resLst) == 1:
            return [resLst[0], resLst[0]]
        else:
           return [resLst[0], resLst[-1]]
    
    
    # 3rd o(logn) algorithm:
    '''
    ause we are locating the leftmost (or rightmost) index containing target (rather than returning true iff we find target), the algorithm does not    terminate as soon as we find a match. Instead, we continue to search until lo == hi and they contain some index at which target can be found.

The other change is the introduction of the left parameter, which is a boolean indicating what to do in the event that target == nums[mid]; if left is true, then we "recurse" on the left subarray on ties. Otherwise, we go right. To see why this is correct, consider the situation where we find target at index i. The leftmost target cannot occur at any index greater than i, so we never need to consider the right subarray. The same argument applies to the rightmost index.
    '''
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1
        
        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]
    
        
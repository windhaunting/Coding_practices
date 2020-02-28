#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:46:16 2018

@author: fubao
"""



# 42. Trapping Rain Water


'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
 compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!


Challenge
O(n) time and O(1) memory
O(n) time and O(n) memory is also acceptable.
Tags

Two Pointers Forward-Backward Traversal Array


Related Problems
Medium Container With Most Water
Hard Trapping Rain Water II
Candy


'''


        
    # reference   https://leetcode.com/problems/trapping-rain-water/solution/


    #1st naive method for each bar, the number of water holds =   min(max_height_left ,max_height_right)−height[i]
    
    # as directed in question. For each element in the array, we find the maximum level of water it can trap after the rain,
    # which is equal to the minimum of maximum height of bars on both the sides minus its own height.
    
    
    #2nd store the result use dynamic programming
    # The water each bar can trap depends on the maximum height on its left and right.
    #Thus scan twice - from left to right, and right to left and record the max height in each direction. The third time calculate the min difference between left/right height and current bar height. 
    #Sum the trapped water to get the final result.
    
    '''
    The water we trapped depends on the left side and right side which has the max height,

    We keep the left side and right side until we find a higher side
    '''
    
class Solution(object):
    # @param A, a list of integers
    # @return an integer
    
    # O(n) time,  O(n) space

    def trap(self, arr):
        height, left, right, water = [], 0, 0, 0
        for i in arr:
            left = max(left, i)
            height.append(left)
        height.reverse()
        for n, i in enumerate(reversed(arr)):
            right = max(right, i)
            water += min(height[n], right) - i
        return water
    
    
# O(n) time,  O(1) space
    
class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, arr):
        left = right = water = 0
        i, j = 0, len(arr)-1
        while i <= j:
            left, right = max(left, arr[i]), max(right, arr[j])
            while i <= j and arr[i] <= left <= right:
                water += left - arr[i]
                i += 1
            while i <= j and arr[j] <= right <= left:
                water += right - arr[j]
                j -= 1
        return water
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 13:53:33 2019

@author: fubao
"""

# facebook

'''
986. Interval List Intersections

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.

'''
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        #1st idea Naively is to use two loop to iteratively traverse to compare every interval in list in A to every interval in B, and then find the overlap, O(N*M).
        
        
        #2nd idea, we can optimize to reduce the comparison time. to O(N+M)
        # because it's disjoint interval and can only compare O(N+M) times use each pointer in M and N
        
        i = 0
        j = 0
        res_interval = []
        while (i < len(A) and j < len(B)):
            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])
            if start <= end:
                res_interval.append([start, end])
            
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res_interval
        
        #3rd idea
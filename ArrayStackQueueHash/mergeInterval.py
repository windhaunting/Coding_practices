#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:33:34 2018

@author: fubao
"""

# 56. Merge Intervals

# facebook

'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

'''


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervalsSort = sorted(intervals, key=lambda inter: inter.start)
        
        ans = [intervalsSort[0]]
        
        for i in range(1, len(intervalsSort)):
            if intervalsSort[i].start <= ans[-1].end:         #merge two intervals
                maxEnd = max(intervalsSort[i].end, ans[-1].end)
                ans[-1].end =  maxEnd
            else:
                ans.append(intervalsSort[i])
        return ans


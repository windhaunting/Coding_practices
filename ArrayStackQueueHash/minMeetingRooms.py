#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:37:51 2018

@author: fubao
"""


# [leetcode] 253. Meeting Rooms II 
'''

Given an array of meeting time intervals consisting of start and end times
 [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

'''
#three methods

#1. using priority queue minHeap of interval end
#1. iterate the interval list;   add the current interval into the minHeap;
#if current interval overlpas with the minHeap's minValue, add room number + 1; 
#else pop from priority;  always add the current interval into the minHeap


#2 using sweeping line algorithm;  based on hash map

#3 not using priority queue

# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

import heapq
from collections import OrderedDict

class Solution:
    # @param {Interval[]} intervals
    # @return {integer}
    
    #1nd priority queue minHeap
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        
        interSorted = sorted(intervals, key = lambda inter: inter.start)
        minNum = 0
        hp = []            #minHeap
        #heapq.heappush(hp, interSorted[0].end)
        for i in range(0, len(interSorted)):

            while hp and hp[0] <= interSorted[i].start:
                print ('hddd', hp[0], interSorted[i].start)
                heapq.heappop(hp)
            heapq.heappush(hp, interSorted[i].end)
            minNum = max(minNum, len(hp))
        
        return minNum


     #2nd  using sweeping line 
    def minMeetingRooms2(self, intervals):
        dic = {}        # sorted by key
        
        for inter in intervals:
            if inter.start not in dic:
                dic[inter.start] = 1
            else:
                dic[inter.start] += 1
                
            if inter.end not in dic:
                dic[inter.end] = -1
            else:
                dic[inter.end] -= 1
                
        ans = 0
        s = 0
        sortedDic = sorted(dic.items())
        for k, v in sortedDic:
            print ("K: ", k)
            s += v
            ans = max(s, ans)
        return ans
             
solutionObj = Solution()
print ('ddd: ', solutionObj.minMeetingRooms2([Interval(0, 30),Interval(5, 10),Interval(8, 20)]))



# transform:
 interval [startTime, stoptime) ----integral time stamps 
  给这样的一串区间I1, I2......In 找出一个time stamp 出现在interval的次数最多。
  startTime <= t< stopTime 代表这个数在区间里面出现过。 
  example： [1,3), [2, 7), [4, 8), [5, 9).  5和6各出现了三次
    
    idea is to use priority get startTime as well  into overlapping lst
    when if interSorted[i].start < heapq.heappop(heap)
    the final overlapping lst has the number that appers most.
    
    
    
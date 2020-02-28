#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 08:52:11 2018

@author: fubao
"""

#
#759. Employee Free Time


'''
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

Example 1:
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation:
There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined.)

Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

'''


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        
        
# https://www.youtube.com/watch?v=VTgF52uGK0Y
#first idea based on virtual merging

'''
 # c++ 
   vector<Interval> employeeFreeTime(vector<vector<Interval>>& schedule) {
      vector<Interval> all;
      for (const auto intervals : schedule)
        all.insert(all.end(), intervals.begin(), intervals.end());
      std::sort(all.begin(), all.end(), 
                [](const Interval& a, const Interval& b){
                  return a.start < b.start;
                });
      vector<Interval> ans;
      int end = all.front().end;
      for (const Interval& busy : all) {
        if (busy.start > end) 
          ans.emplace_back(end, busy.start);  
        end = max(end, busy.end);
      }
      return ans;
    }
};
      
'''    

# reference: https://leetcode.com/problems/employee-free-time/solution/
# 2nd sweeping line:
    
        def employeeFreeTime(self, avails):
        OPEN, CLOSE = 0, 1

        events = []
        for emp in avails:
            for iv in emp:
                events.append((iv.start, OPEN))
                events.append((iv.end, CLOSE))

        events.sort()
        ans = []
        prev = None
        bal = 0
        for t, cmd in events:
            if bal == 0 and prev is not None:
                ans.append(Interval(prev, t))

            bal += 1 if cmd is OPEN else -1
            prev = t

        return ans

# 3 use priority 
     #   reference: https://leetcode.com/problems/employee-free-time/solution/
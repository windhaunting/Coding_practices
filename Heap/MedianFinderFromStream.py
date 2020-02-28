#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:30:40 2018

@author: fubao
"""



# 295. Find Median from Data Stream

'''


Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2

'''

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        

    def findMedian(self):
        """
        :rtype: float
        """
        
        

# https://leetcode.com/problems/find-median-from-data-stream/solution/

    
    # use two prioroty queue a maxheap and minheap to achive findMedian function with O(1) time
    
    # Adding a number num:

   # Add num to max-heap lo. Since lo received a new element, we must do a balancing step for hi. So remove the largest element from lo and offer it to hi.
   # The min-heap hi might end holding more elements than the max-heap lo, after the previous operation. We fix that by removing the smallest element from hi and offering it to lo.
#The above step ensures that we do not disturb the nice little size property we just mentioned.
    
    
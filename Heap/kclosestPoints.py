#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 22:06:10 2019

@author: fubao
"""

# facebook

'''
973. K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

'''


import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
    # idea 1 naive way is to calculate all the points' distance to the original point (0, 0)'s distance and sort them
    
    # idea to save some space and the time of sorting, use a heap (max heap) to store only k point, if any point come, decide to insert into the heap or not
    
    # define a max heap
    
        heap = []      # min heap for heapq, so multiply -1 to become maxheap

        ind = 0
        while (ind < len(points)):
            dist = self.calculateDistanceToOrigin(points[ind])
            if ind < K:
                heapq.heappush(heap, (-1*dist, points[ind]))
            else:
                # compare
                minVal = -1*heap[0][0]
                if dist < minVal:
                    # remove top
                    heapq.heappop(heap)
                    #push in
                    heapq.heappush(heap, (-1*dist, points[ind]))
            ind += 1
                        
        return [ele[1] for ele in heap]
    
    def calculateDistanceToOrigin(self, point1):
        
        dist = point1[0]**2 + point1[1]**2
        return dist
    
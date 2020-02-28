#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 09:41:41 2018

@author: fubao
"""

#  755. Pour Water


#  https://leetcode.com/problems/pour-water/description/
'''
We are given an elevation map, heights[i] representing the height of the terrain at that index. The width at each index is 1. After V units of water fall at index K, how much water is at each index?

Water first drops at index K and rests on top of the highest terrain or water at that index. Then, it flows according to the following rules:

If the droplet would eventually fall by moving left, then move left.
Otherwise, if the droplet would eventually fall by moving right, then move right.
Otherwise, rise at it's current position.
Here, "eventually fall" means that the droplet will eventually be at a lower level if it moves in that direction. Also, "level" means the height of the terrain plus any water in that column.
We can assume there's infinitely high terrain on the two sides out of bounds of the array. Also, there could not be partial water being spread out evenly on more than 1 grid block - each unit of water has to be in exactly one block.

'''
#


# https://www.youtube.com/watch?v=sgDdhNTByLQ&index=8&list=PLLuMmzMTgVK66JImslfqAJLovRAyQKAas

class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        
      
    def drop(h, K):
      best = K
      for d in (-1, 1):           #shift left or right
        i = K + d
        while i >= 0 and i < len(h) and h[i] <= h[i - d]:
          if h[i] < h[best]:
            best = i
          i += d
        if best != K:
          break
      heights[best] += 1
 
    for _ in range(V):
      drop(heights, K)
    return heights
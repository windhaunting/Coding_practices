#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 21:24:20 2018

@author: fubao
"""

'''
# 554. Brick Wall  facebook

There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Example:
Input: 
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
Output: 2
Explanation: 

Note:
The width sum of bricks in different rows are the same and won't exceed INT_MAX.
The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000]. Total number of bricks of the wall won't exceed 20,000.

'''

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        
        #1st naive way get the accumulated sum and figure out the way each number is in the list
        '''
        e.g.
        input = 
            [[1,2,2,1],
         [3,1,2],
         [1,3,2],
         [2,4],
         [3,1,2],
         [1,3,1,1]]
            
            
        we get accumulated sum for the list;  no need the consider the last sum in each row
        [[1, 3, 5],
         [3,4],
         [1,4],
         [2]
         [3,4]
         [1,4,5]]
        
        then we get the maximum number of each element appearing in all rows, the minimum number is just the rows number - maximum number.
        '''
        
        if wall is None:
            return 0
        sumWall = []
        nums = set()
        for i in range(0, len(wall)):
            wl = wall[i]
            nums.add(wl[0])
            for j in range(1, len(wl)-1):     # no need the consider the last sum in each row, 
                wall[i][j] =  wall[i][j] + wall[i][j-1]
                nums.add(wall[i][j])
                
        maxCnt = -1
        for n in nums:
            cnt = 0
            for i in range(0, len(wall)):
                if n in wall[i][:-1]:
                    cnt += 1
                #print ("cnt: ", wall[i][:-1], cnt, maxCnt)      #, wall, maxCnt)
            maxCnt = max(cnt, maxCnt)             
        #print ("wall: ", nums)      #, wall, maxCnt)
        return len(wall) - maxCnt
        '''
        
        #2nd the same idea, but we use hashmap to save time. PASSED
        
        if wall is None:
            return 0
        sumWall = []
        numsDict = defaultdict(int)
        for i in range(0, len(wall)):
            wl = wall[i]
            numsDict[wl[0]] += 1
            for j in range(1, len(wl)-1):     # no need the consider the last sum in each row, 
                wall[i][j] =  wall[i][j] + wall[i][j-1]
                numsDict[wall[i][j]] += 1
        ans = 2**32
        
        for k, v in numsDict.items():
            ans = min(ans, len(wall) - v)
        return ans if len(numsDict) !=1 else len(wall)        # special case, e.g. [[1],[1],[1]], return 3 not 1
        

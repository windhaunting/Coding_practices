#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 10:04:17 2018

@author: fubao
"""


# 632. Smallest Range


'''

You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Note:
The given list may contain duplicates, so ascending order means >= here.
1 <= k <= 3500
-105 <= value of elements <= 105.
For Java users, please note that the input type has been changed to List<List<Integer>>. And after you reset the code template, you'll see this point.

'''




from heapq import *

class Solution:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        #1ST NAIVE WAY IS to combine all the element in k list together into one list C; also records its index belonging to which index; then sort C;  next we use two loops iterate the list for each pair (i, j) and use a count pointer to indicate whether all k list has been obtained, if so,update the range between (i, j)
        
        
        #2nd way consider the sorted element in each list;
        # set up a list indLst size == k, each intialized with 0 index; k = len(nums)
        # first we get the min and max value from each sorted list num at the correspoinding index position in indLst; update the rnage; the range must have contained at least one element in each list in nums list
        # find the index of the minimum element in nums lists;  and increase the index + 1 in the correspoinding indLst
        # worst time complexity is O(n*k), n is the the total number of elements in the list
        
        #3rd in the 2nd method, each time we have to traverse k elements to get min and max values
        # we could use priority queue (minHeap) to get minvalue, the max value is max(lastMax, newComingElement);
        # reduce time complexity? o(k) time?
        
        # ref: https://leetcode.com/problems/smallest-range/solution/
        if nums is None or len(nums)==0:
            return None
        
        que = []
        
        lastMax = 0
        k = len(nums)
        
        indLst = [0]*k
        
        minVal = 2**32
        maxVal = -2**32
        ran = 2**32    #minimum range
        for i in range(0, k):
            heappush(que, (nums[i][indLst[i]], i))
            maxVal = max(maxVal, nums[i][indLst[i]])

        minVal = que[0][0]
        minInd = que[0][1]
        indLst[minInd] += 1

        lastMax = maxVal
        ran = min(maxVal - minVal, ran)
        resLst = [minVal, maxVal]
        while indLst[minInd] < len(nums[minInd]):
            #update the index with the minimum element
            heappop(que)
            heappush(que, (nums[minInd][indLst[minInd]], minInd))

            maxVal = max(lastMax, nums[minInd][indLst[minInd]])
            minVal = que[0][0]
            minInd = que[0][1]
            indLst[minInd] += 1
                
            lastMax = maxVal
            if maxVal - minVal < ran:
                ran = maxVal - minVal
                resLst = [minVal, maxVal]
        return resLst
    
        
    
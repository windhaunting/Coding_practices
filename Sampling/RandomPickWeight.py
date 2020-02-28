#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 00:10:32 2019

@author: fubao
"""


# facebook  

'''
528. Random Pick with Weight

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
'''



import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w

    def pickIndex(self) -> int:
        #idea 1. copy the times of each index weight into a new array, in the new array, each value is picked randomly and equally, which has the same probability as the number of the original weight.
        # problem too costly for the space.
        
        # NOT PASSED, DON'T KNOW WHY YET. IT SEEMS WORK. idea 2 use prefix sum, accumulated sum of weight 
        # e.g.  [1,3,2]  => index [0,1,2], we get prefix sum[1,4,6]
        # then we pick number from 0 to 5, if it's 1, index 0, if it's 2-4, return index 1, if it's 5-6 
        #return index 2; each number has a proportional weight = 3
        # because it's ordered, we can use binary search
        
        if not self.w or len(self.w) == 0:
            return 0
        # prefix sum
        for i in range(1, len(self.w)):
            self.w[i] +=self.w[i-1]
        
        # generate a random number
        v = random.randint(0, self.w[-1])
        #bfs search
        ind = self.bfs(self.w, v)
        
        for i in range(0, self.w[-1]):
            ind = self.bfs(self.w, i)
            print ("i : ", i, ind)
        return ind
    
    def bfs(self, w, v):
        l = 0
        r = len(w)-1
        while (l < r):
            mid = l + (r-l)//2
            if v >= w[mid]:
                l = mid + 1
            else:
                r = mid
        return r                     
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 20:21:30 2018

@author: fubao
"""

#31. Next Permutation

fail
1,2,3 → 1,3,2

traverse  backward
 2 < 3; => 3 -2   now 1 3 2
 if 1 < 3; no move
 

e.g.
 1 3 2  ->  2 1 3
 
 if 3 > 2 ; move pointer 2 3   now  1 2 3; if 1 < 2;  no move?  have to move 2 1 3:
     
e.g.  3 2 1
  -> 3 1 2;      3 > 1;  1 3 2
     
'''
'''

6 4 5 8 7 1     =>  find 5 first ;  swap 5 vs 7 (first igger than 5 after 5's position) '  6 4 7 8 5 1   
                                                
                                                =>  then sort after 5's positon ' 6 4 7 1 5 8
    
 
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1



# for another question about previous permuation number

6 4 7 1 5 8     =>   6 4 5 8 7 1          Similar idea

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        #from back traverse and find the first numer n in non-ascending order ;
        #and swap with the smallest one after n's position bigger than the found n ;
        #then reverse the first several number before n (called found subarray) 
        
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                
                #find the smallest one bigger than the found n
                minInd = i
                #print ('i: ', i)
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] <= nums[minInd] and nums[j] > nums[i-1]:
                        #minVal = nums[j]
                        minInd = j
                        break
                #swap the minInd
                tmp = nums[minInd]
                nums[minInd] = nums[i-1]
                nums[i-1] = tmp
                #print (' nums:   ', nums, nums[i::],i)
                # reverse the found subarray
                nums[i::] = nums[i::][::-1]
                
                return

        #else
        nums[::] = nums[::][::-1]              #nums.reverse()
    
    
            
                
                
        
        
        
        
        
        
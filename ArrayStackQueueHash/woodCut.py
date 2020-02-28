#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 11:02:38 2018

@author: fubao
"""



# http://www.lintcode.com/en/problem/wood-cut/
#

'''
Given n pieces of wood with length L[i] (integer array). 
Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. 
What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.
Example
For L=[232, 124, 456], k=7, return 114.
Note
You couldn't cut wood into float length.

Challenge
O(n log Len), where Len is the longest length of the wood.

'''

'''
find the maximum length of wood cut

For L=[232, 124, 456], k=7, return 114.

232/114 = 2 ; 124/2 = 1;       456/114 = 4;         2+1+4=7

naive way is to search maximum length from 1 to check how many equal pieces >=k

improve: not starting from 1; starting from min(L) / (n/k+1) and then search; here   124 /(7/3+1) = 41;
startin from 41;    the time complexity is o(nLen);  Len is the longest length of the wood. too high


binary earch method:
    
'''

class Solution:
    """
    @param: L: Given n pieces of wood with length L[i]
    @param: k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if sum(L) < k:
            return 0
            
        start = int(min(L) /(int(k/len(L))+1))
        
        print ("minStart: ", start)
        
        end = max(L)
        
        while(start <= end):
            
            mid = int(start + (end-start)/2)        #possible maximum length of the small pieces
            
            #get number k
            num = sum([int(i/mid) for i in L])
            print("cutMaxLen", mid, num, start, end)

            if num >= k:       #enough, but maybe not the maximum length
                start = mid+1
            else:
                end = mid-1
                
        print ("start: ", start)
        return start-1

L = [232, 124, 456]
k = 7
SolutionObj = Solution()
SolutionObj.woodCut(L,k)


        
        
        
        
        
        
        
        
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 21:21:53 2018

@author: fubao
"""

#classific problem:  kth smallest or largest number in an array (unsorted) given

#or topk  smallest or largest number

#  215. Kth Largest Element in an Array

'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

'''

import heapq

def findKthLargest(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    
    #1st sort , too naive, not recommended
    
    '''
    4 3 2 5
    2. 2nd method partition method   inside loop, only swap between smaller and bigger value;  no swap exchange itself; pivot swap after finishing loop
    e.g 4, 3, 5, 6 1 2;  l = 0, r= 4, i = l= 0, j = l+1= 1; pivot = 4 as leftmost
    =>  4, 3, 5, 6, 1, 2   j=1, i=0 ; ==> i=1  no swap
    =>  4, 3, 5, 6, 1, 2  j = 2
    =>  4, 3, 5, 6, 1, 2  j = 3
    =>  4, 3, 1, 6, 5, 2   j = 4, i = 1  ==> i=2 ; swap
    =>  4, 3, 1, 2, 5, 6   j= 5, i=2; => i=3  swap
    =>  2, 3, 1, 4, 5, 6
    quickselect.    set the pivot  (e.g. the first element or random element ） and rearrange all the element less than pivot to be in the left, bigger than pivot to be in the right;    then compare with the pivot index with k to decide to go next in the left part or right part to recursively do the same thing
    '''
    '''
    #select left of index is less than num[index] ,  for kth smallest quickselect
    def select(nums, l, r, index):
        if r == l:
            return nums[l]
        #pivot index
        pind = random.randint(l, r)           #randomly select has high prob of o(nlogn) time complexity
        nums[l], nums[pind] = nums[pind], nums[l]   #move pivot to the beginning of the
        
        #partition around pivot
        i = l
        for j in xrange(l+1, r+1):
            if nums[j] < nums[l]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[l] = nums[l],nums[i] 
        
        if index == i:
            return nums[i]
        elif index < i:
            return select(nums, l, i-1, index)
        else:
            return select(nums, i+1, r, index)
        
    index = len(nums) - k
    if nums is None or len(nums) < 1:
        return 0
    return select(nums, 0, len(nums)-1, index)
    '''
    
    '''
    The performance of quickselect is dependant on the selection of the pivots. 
    In the worst case, the time complexity is O(n^2),
    but with a good pivot selection strategy, the average time complexity is O(n). n + n/2 + n/4 + n/8 + ...+ 1 <= O(2n)
    The worst-case time taken by a randomized quick-select is not O(n). It is O(n^2).
    '''
    
    
    #3rd method,  python heaq only support min-heap;   O(k) +  O((n-k) * logk) worst
    #if built-in heapq  (priority queue) is allowed in python,
    h = []
    for n in nums:          #only store k element in the heap
        if len(h) < k:                            #O(k)  time if we not consider heappush heapify time
            heapq.heappush(h, n)     #minheap
        elif n > h[0]:                          # complexity The step 2 is O((n-k) * logk)

                heapq.heappop(h)
                heapq.heappush(h, n)    
        
    return h[0]

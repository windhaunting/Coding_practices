#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 00:51:41 2018

@author: fubao
"""



# segment tree implementation

#   https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/

# e.g.  307. Range Sum Query - Mutable

'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

'''

'''
**** important to understand that if we assume the number of calls to update and sumRange function is distributed evenly.
'''


'''
线段树是用于存放间隔或者线段的树形数据结构，它允许快速的查找某一个节点在若干条线段中出现的次数.
时间复杂度:
区间查询: O(log(n))
更新: O(log(n))
'''
# here is range sum segment tree, range minimum can also be used with segment tree
# find minimum range of of a subarray in o(logn)
# https://www.youtube.com/watch?v=ZBHKZF5w4YU
#1st use tree left right node to implementation segment tree
#2nd use array  i,  2*i + 1, 2*i + 2

# 1st method
class Node(object):
    def __init__ (self, start, end):
        self.start = start           # start index of a node
        self.end = end              # end index of a node
        self.sum = 0
        self.left = None            # left node
        self.right = None           # right node
        
class NumArray(object):
    def __init__ (self, nums):
        '''
        :type nums: list[int]
        '''
        self.root = None
        
    def createTree(self, nums, l, r):
        '''
        create segment tree
        '''
        
        #base case
        if l > r:
            return None
        
        # leaf node:
        if l == r:
            nd = Node(l, r)
            nd.sum = nums[l]
            return nd
        
        # otherwise internal node
        mid = l + (r-l)//2   #segment half
        
        #recursively create tree
        left = self.createTree(nums, l, mid)
        right = self.createTree(nums, mid+1, r)
        
        root = Node(l, r, left.sum + right.sum, left, right)
        return root
        
    def updateNode(self, index, val):
        '''
        update an array index value
        here use recursive way to update
        '''
        def updateValHelper(root, index, val):
            # base case, the leaf node encountered
            if root.start == root.end:
                root.sum = val
                return val
            
            mid = root.start + (root.end - root.start) // 2
            
            if index <= mid:       #go left
                updateValHelper(root.left, index, val)
                
            else:
                updateValHelper(root.right, index, val)
                
            #update parent sum
            root.sum = root.left.sum + root.right.sum
            
            return root.sum
        
        return updateValHelper(self.root, index, val)
            
    def rangeSumQuery(self, lInd, rInd):
        '''
        query content between left and right index
        '''
        def rangeSumHelper(root, lInd, rInd):
            
            #if lInd > root.end or lInd < root.start:
            #    return 0
            
            #inside
            if lInd == root.start and lInd == root.end:
                return root.sum
            
            mid = root.start + (root.end - root.start) // 2
              
            if rInd <= mid:
                return rangeSumHelper(root.left, lInd, rInd)
            
            elif lInd >= mid + 1:
                return rangeSumHelper(root.right, lInd, rInd)
        
            else:
                #overlapping with both 
                return rangeSumHelper(root.left, lInd, mid) + rangeSumHelper(root.right, mid+1, rInd)


        return rangeSumHelper(self.root, lInd, rInd)
    
    
nums = [1,2,3,4,5]
NumArrayObj = NumArray(nums) 
NumArrayObj.root = NumArrayObj.createTree(nums, 0, len(nums)-1)

print ("range sum " , NumArrayObj.root.left.sum)

print ("range sum " , NumArrayObj.rangeSumQuery(2,4))
print ("range sum " , NumArrayObj.rangeSumQuery(1,1))

NumArrayObj.updateNode(2,10)
print ("range sum " , NumArrayObj.rangeSumQuery(2,4))


# 2nd way to implement  use array

# reference: https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/




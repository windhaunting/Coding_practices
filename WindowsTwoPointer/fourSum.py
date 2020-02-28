#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:54:29 2018

@author: fubao
"""


# 18. 4Sum


'''

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        '''
        if not nums:
            return []
        resLst = []
        #nums.sort()
        for i in range(0, len(nums)):
            d1 = target - nums[i]
            for j in range(i+1, len(nums)):
                d2 = d1 - nums[j]
                indMap = {}
                #using 2 sum to get d1
                
                for k in range(j+1, len(nums)):
                    d3 = d2 - nums[k]
                    if d3 in indMap:
                        innerLst = sorted([nums[i], nums[j], nums[k], d3])
                        if innerLst not in resLst:
                            resLst.append(innerLst)
                    else:
                        indMap[nums[k]] = j
        return resLst
        '''
        
        
        # is this o(n^2) ?... create pair hash first before iterations 
        if not nums:
            return []
        resLst = []
        #create pair hash
        
        pairHash = {}
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                s = nums[i] + nums[j]
                if s not in pairHash:
                    pairHash[s] = [[i, j]]
                else:
                    pairHash[s].append([i,j])
                    #pairHash[s].append(i)
                    #pairHash[s].append(j)        #
        #print ('hashPair: ', pairHash)           
        for i in range(0, len(nums)):
            d1 = target - nums[i]
            for j in range(i+1, len(nums)):
                d2 = d1 - nums[j]
                if d2 in pairHash:
                    indexLst = pairHash[d2]
                    print ('index: ', indexLst, i, j)  
                    for ls in indexLst:
                        if i not in ls and j not in ls:
                            innerLst = []
                            innerLst.append(nums[i])
                            innerLst.append(nums[j])
                            innerLst.append(nums[ls[0]])
                            innerLst.append(nums[ls[1]])
                            innerLst.sort()
                            if innerLst not in resLst:
                                resLst.append(innerLst)
        return resLst      
                              
                
        
# 3rd use hashmap ;   time:  O(n^3) ;         

from collections import defaultdict

def find_array_quadruplet(arr, s):
   if not arr:
       return []
      
   dic = defaultdict(int)
   for a in arr:
       dic[a] += 1
   
   for i in range(len(arr)):
        dic[i] -= 1
        for j in range(i+1, len(arr)):
            dic[j] -= 1
            for k in range(j+1, len(arr)):
                dic[k] -= 1
                diff = s - (arr[i] + arr[j] + arr[k])
                #print ("aaaa: ", arr[i], arr[j], arr[k])
                if diff in dic and dic[diff] > 0:
                   ans = [arr[i], arr[j], arr[k], diff]
                   #print ("ans: ", ans)
                   return ans
   return []
   
arr = [4,4,4,2]
s2 = 14

print(find_array_quadruplet(arr, s2))

arr = [4,4,4,4,2,8]
s2 = 16

print(find_array_quadruplet(arr, s2))

arr = [4,4,4,1, 2,8]
s2 = 15

print(find_array_quadruplet(arr, s2))  



'''
  o(n^3)
  
  [1,2,3,4,5, 6]
  
  nlogn  +n^3  = o(n^3)
  
  sum = 11
  o(1)
  two loop i, j
    arr[i], arr[j]
     diff = sum - ( arr[i]_+ arr[j])
      two pointer,  k, l
      k->1
      l->6
      sum arr[k] + arr[l]  > diff
          l -= 1
                           < diff
          k += 1
       until k ==l
      
      
arr1 = [2,7,4,0,9,5,1,3]
arr2 = [4,4,4]
s2 = 12
arr3 = [4,4,4,2]
s3 = 16
arr3 = [4,4,4,4]
s3 = 16

# range1

print(find_array_quadruplet(arr2, s2))


'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:56:21 2019

@author: fubao
"""

# permutation of backtracking

# given a list with unique number ,generate the permutation of list

#e.g. [1, 2, 3] ==> [1,2,3], [1,3,2], [2,1,3],[2,3,1], [3,1,2], [3,2,1]


# reference: 
# https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/


        
#idea 1:  code 1:  get the permutated list of the nums backtracking idea

cnt = 0  
res_lst = []
def permutation(nums):
    # nums has unique numbers
    # corner case ignored
    
    def recurHelper(nums, N, visited, cur_lst, pos):
        if pos >= N:
            global cnt
            cnt += 1
            global res_lst
            res_lst.append(cur_lst)
            #cur_lst.clear()
            #print ("res_lst: ", res_lst)
            return
        
        for i in range(0, N):
            if visited[nums[i]] == 0:
                visited[nums[i]] = 1
                #print ("cur_lst: ", cur_lst)
                recurHelper(nums, N, visited, cur_lst + [nums[i]],  pos+1)
                visited[nums[i]] = 0
                
    N = len(nums)
    visited = [0] * (N+1) 
    #cnt = 0
    cur_lst = []
    recurHelper(nums, N, visited, cur_lst, 0)
    
    print ("cnt, res_lst: ", cnt, res_lst)
   
permutation([1,2,3,4])



#idea 2:  code 2 idea from 
# # https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

def permuationArray(nums):
    
    def dfsPermutation(nums, l, r):
        
        if l == r:
            self.res_list.append(nums)
            print ("ssss: ", self.res_list)
        else:
            for i in range(l, r+1):
                nums[l], nums[i] = nums[i], nums[l]          # swap operation in the python
                #print ("before l, r: ", i, l, r, res_list)
                self.dfsPermutation(nums, l+1, r)

                #print ("l, r: ", i, l, r, res_list)
                nums[l], nums[i] = nums[i], nums[l]  
                
     # reference: https://www.geeksforgeeks.org/python-select-random-value-from-a-list/
    dfsPermutation(nums, 0, len(nums)-1)
    


#idea 3: Code 3:

# reference 3: https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
    
# Python function to print permutations of a given list 
def permutation(lst): 
  
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
       m = lst[i] 
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = lst[:i] + lst[i+1:] 
  
       # Generating all permutations where m is first 
       # element 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 



# code 3:  
#if we get need to get the number of permutated list
cnt = 0  

def permutation(nums):
    # nums has unique numbers
    # corner case ignored
    
    def recurHelper(nums, N, visited,  pos):
        if pos >= N:
            global cnt
            cnt += 1
            print ("cntttt: ", cnt)
            return
        
        for i in range(0, N):
            if visited[nums[i]] == 0:
                visited[nums[i]] = 1
                recurHelper(nums, N, visited, pos+1)
                visited[nums[i]] = 0
                
    N = len(nums)
    visited = [0] * (N+1) 
    #cnt = 0
    recurHelper(nums, N, visited, 0)
    
    print ("cnt: ", cnt)
   
permutation([1,2,3])


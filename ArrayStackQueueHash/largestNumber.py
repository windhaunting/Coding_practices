#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 22:44:58 2018

@author: fubao
"""

# 179. Largest Number


'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"


Note: The result may be very large, so you need to return a string instead of an integer.

'''
# examine  sorting algorithm


def largestNumber(nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    
    #use a sorting algorithm e.g. bubble sort the algorithm to sort according to string
    # this doesn't work
    '''
    strLst = [str(a) for a in nums]
    
    print ("strLst: ", strLst)
        
    strLstA = sorted(strLst, reverse=True)
    ans = "".join(strLstA)
    print ("strLstA: ", strLstA)
    '''
    
    # case 1  34 vs 34
    #case2: 3 vs 34  ;    34 vs 3;        30 vs 3;  3 vs 30
    # 824 vs 8247
    #case3:  20 vs 1;       
    
    # this works:
    # compare the element by ourselves according to the rule of largest number first
    
    if nums is None or len(nums) == 0:
        return ''
    
    for i in range(len(nums)-1, -1, -1):
        for j in range(len(nums)-1, len(nums)-i-1, -1):
            #compare element 1, 2
            e1 = str(nums[j-1])
            e2 = str(nums[j])
            #print ("e1, e2: ", e1, e2, nums)
            if len(e1) == len(e2):
                if e1 < e2:
                    #swap
                    t = nums[j]
                    nums[j] = nums[j-1]
                    nums[j-1] = t
            else:
                k = 0
                while (k < len(e1) and k < len(e2)):
                    if e1[k] < e2[k]:
                        #swp and break
                        t =  nums[j]
                        nums[j] = nums[j-1]
                        nums[j-1] = t
                        break
                    elif e1[k] == e2[k]:
                        k += 1
                    else:
                        break
                print ("k: ", k, e1, e2)
                if k == len(e1):
                    m = 0
                    while (m < len(e2)):
                        if e2[-1] > e2[m]:
                            print ("kvvvvvv: ", k, e1, e2)
                            t =  nums[j]
                            nums[j] =  nums[j-1]
                            nums[j-1] = t
                            break
                        elif e2[k] == e2[m]:
                            m += 1
                        else:
                            break
                
                elif k == len(e2):
                    m = 0
                    while (m < len(e1)):
                        if e1[-1] < e1[m]:
                            print ("kdddvvv: ", k, e1, e2)
                            t =  nums[j]
                            nums[j] =  nums[j-1]
                            nums[j-1] = t
                            break
                        elif e1[k] == e1[m]:
                            m += 1
                        else: 
                            break
                        
    ans = ''
    for n in nums:
        if n == 0 and ans == '':
            continue
        ans += str(n)
    #print ("nums: ", nums)
    return '0' if len(ans) == 0 else ans 



def largestNumber2(nums):


    if nums is None or len(nums) == 0:
        return ''
    
    for i in range(len(nums)-1, -1, -1):
        for j in range(len(nums)-1, len(nums)-i-1, -1):
            #compare element 1, 2
            e1 = str(nums[j-1])
            e2 = str(nums[j])
            #print ("e1, e2: ", e1, e2, nums)
            if e1+e2 < e2+e1:
                #swap 
                t = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = t

    ans = ''
    for n in nums:
        if n == 0 and ans == '':
            continue
        ans += str(n)
    #print ("nums: ", nums)
    return '0' if len(ans) == 0 else ans 


# 3rd more elegant way to write the code
    
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber3(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

 
a = [3,30,34,5,9]
#a = [10, 2]
#a = [12,128]
#a = [128,12]

#a = [20,1]
#a = [0,0]
#a = [824, 8247]
#a = [121,12]
a = [883, 8]

#ans = largestNumber(a)
ans = largestNumber2(a)

print ("ans: ", ans)
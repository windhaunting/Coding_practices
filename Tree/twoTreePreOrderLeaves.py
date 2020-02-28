#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:25:59 2018

@author: fubao
"""



'''
# Given two pre-order traversal arrays of two binary search tree respectively, 

find first pair of non-matching leaves. 
Follow Up: If they are general binary trees instead of BSTs, 
could you solve it? give out your reason. 

'''


def get_leaves(pre_order, leaves):
    if not pre_order:
        return
    
    root = pre_order[0]
    if len(pre_order) == 1:
        leaves.append(root)
        return
        
    left_start = None
    left_end = None
    right_start = None
    righEnd = None
    for i in range(1, len(pre_order)):
        if not left_start and pre_order[i] <= root:
            left_start =  i
        
        if not right_start and pre_order[i] > root:
            right_start =  i
    
    if left_start:
        if right_start: left_end = right_start
        else: left_end = len(pre_order)
        get_leaves(pre_order[left_start:left_end], leaves)
    
    if right_start:
        righEnd = len(pre_order)
        get_leaves(pre_order[right_start:righEnd], leaves)

a = [5, 3, 2, 1, 4, 7, 6, 8]
a_leaves =[]
get_leaves(a, a_leaves)
print ("leaves: ", a_leaves)
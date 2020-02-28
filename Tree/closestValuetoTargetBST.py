#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:05:07 2018

@author: fubao
"""



#  Closest Binary Search Tree Value


'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

'''

class Solution(object):
    def closestValue(self, root, value):
        
        
        # gap
        gap = abs(root.val - value)
        ans = root
        while root is not None:
            if root.val == value:
                return root.val
            elif value < root.val:
                if abs(root.val - value) < gap:
                    ans = root
                    gap = abs(root.val - value)
                root = root.left
            else:
                if abs(root.val - value) < gap:
                    ans = root
                    gap = abs(root.val - value)
                root = root.right
        return ans.val
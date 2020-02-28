#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 00:24:56 2018

@author: fubao
"""



# cycle sort


 reference:  https://www.geeksforgeeks.org/cycle-sort/
 
 
 '''
 
We one by one consider all cycles. We first consider the cycle that includes first element.
 We find correct position of first element, place it at its correct position, say j.
 We consider old value of arr[j] and find its correct position, we keep doing this till

 all elements of current cycle are placed at correct position, i.e., we don’t come back to cycle starting point
 
 
 '''
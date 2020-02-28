#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:27:43 2018

@author: fubao
"""

# nth root

# https://www.pramp.com/question/jKoA5GAVy9Sr9jGBjzN4


'''
function root that calculates the n’th root of a number. The function takes a
 nonnegative number x and a positive integer n, and returns the positive n’th root
 of x within an error of 0.001
 (i.e. suppose the real root is y, then the error is: |y-root(x,n)| and
 must satisfy |y-root(x,n)| < 0.001).
'''


#1st use binary search
'''
x = 7, n = 3
0, 1, 2  3, 4, 5, 6, 7

'''

def nthRoot(x, n):
    
    l = 0
    r = x # max(1, x)
    mid = l + (r-l)/2.0
    while (mid-l > 0.001):
        
        #if l-mid > 0.001:
        #    return mid
        print ("mid: ", mid)
        if mid**n < x:
            l = mid
        if mid**n > x:
            r = mid
        mid = l + (r-l)/2.0
    return round(mid, 3)

print ("answer: ", nthRoot(7, 3))

print ("answer: ", nthRoot(9, 2))



'''
x = 7, n = 3

l     r    mid
0,    7,    3.5

0     3.5   1.75
1.75  3.5   2.625
....

'''

#2nd use newton method

# reference: 

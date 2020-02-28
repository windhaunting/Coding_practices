#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 13:11:34 2018

@author: fubao
"""


# 50. Pow(x, n) power

'''
Implement pow(x, n).


Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100

'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        '''
        # directly multiple; time limit exceeded
        i = 0
        res = 1
        while ( i < abs(n)):
            res = res * x
            i += 1
        
        if n < 0:
            res = 1/res
        return res
        '''
        
        '''
        #2 use binary search idea to do the pow(x, n)
        # there is n times ; each time decrease n; x^2 ' e.g 3^4  => (3*3 )^2
        if n == 0: 
            return 1
        if n < 0:
            n  = -n
            x = 1/x
        if n%2 == 0:
            return self.myPow(x*x, n/2) 
        else:
            return x*self.myPow(x*x, n/2) 
        
        '''
        
        #iterative version
        
        def stepDown(n):
            while n>=1:
                yield n
                n = n/2
                
        res = 1.0
        for i in stepDown(abs(n)):
            if (i % 2 != 0):
                res *= x
            x *= x
        return res if n >= 0 else 1/res
    
        
        '''
        def stepDown(n):
            while n>1:
                yield n
                n = n/2
        '''
        '''
        def my_range(start, stop, f):
            x = start
            while x < stop if stop > start else x > stop:
                yield x
                x = f(x)
        >>> list(my_range(1, 1024, lambda x: x*2))
        [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
        
        '''
        #reference:  http://www.cnblogs.com/grandyang/p/4383775.html    

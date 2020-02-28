#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 13:30:11 2018

@author: fubao
"""


#  372. Super Pow  power mod pow mod

'''
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024
'''


class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        '''
        #1st fail TLE or overflow of integer range  if we use the pow (x, n) idea
        def helper(x, n, k):
            if n == 0:
                return 1
            return helper(x*x, n/2, k) if n %2 == 0 else x*helper(x*x, n/2, k)
        
        #get integer from b
        inb = 0
        for i in range(len(b)-1, -1, -1):
            inb += b[i] * 10**(len(b)-1 -i)
            
        #print('inb :', inb)
        return helper(a%1337, inb, 1337) % 1337
        '''
        
        #1st try again
        '''
        def helper(x, n, k):
            ans = 1
            x = x % k
            i = 0
            while (i < n):
                ans = (ans *x) % k
                i += 1
            return ans % k
        
        
        #get integer from b
        inb = 0
        for i in range(len(b)-1, -1, -1):
            inb += b[i] * 10**(len(b)-1 -i)
            
        #print('inb :', inb)
        return helper(a, inb, 1337)
        '''
      
        '''
        #2nd success
        ans = 1
        mod = 1337
        for bi in b[::-1]:
            ans = ans * a ** bi % mod
            a = a ** 10 % mod
        return ans        
        '''
        
        
        
        #3rd time  quick pow, super pow using distributive modulo
        # (A+B)modM=(AmodM+BmodM)modM
        #(a ⋅ b) mod m =  [(a mod m) ⋅ (b mod m)] mod m

        ans = 1
        k = 1337
        inb = 0
        for i in range(len(b)-1, -1, -1):
            inb += b[i] * 10**(len(b)-1 -i)
        a = a % k
        
        while (inb > 0):
            if inb % 2 == 1:
                ans *= a % k
            ans = ans % k
            inb /= 2
            a = (a * a) %k

        return ans
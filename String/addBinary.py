#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 17:46:03 2018

@author: fubao
"""


#  67. Add Binary

'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        '''
        # complement to the same length and sum
        la = len(a)
        lb = len(b)
        
        while( la > lb):
            b = '0' + b
            lb += 1
        while (la < lb):
            a = '0' + a
            la += 1
            
        c = 0
        r = ""
        i = la-1
        while(i >= 0):
            e1 =int(a[i])
            e2 = int(b[i])
            
            d = (e1 + e2 + c)%2
            c = (e1 + e2 + c)/2
            r = str(d) + r
            i -= 1
        if  c == 1:
            r = str(c) + r
        return r
        '''
            
            
        #2nd pythonic way:
        return bin(int(a, 2) + int(b, 2))[2:]
    


'''
other solutions:

I assume using int and str is okay, I think this is easy to understand.

def addBinary(self, a, b):
    result = ''
    index = 0
    
    carry = '0'
    while index < max(len(a), len(b)) or carry == '1':
        num_a = a[-1 - index] if index < len(a) else '0'
        num_b = b[-1 - index] if index < len(b) else '0'
        
        val = int(num_a) + int(num_b) + int(carry)
        result = str(val % 2) + result
        
        carry = '1' if val > 1 else '0'
        index += 1

    return result
================== update ===============

No int and str version.

class Solution:
# @param a, a string
# @param b, a string
# @return a string
# 75ms
def addBinary(self, a, b):
    result = ''
    index = 0
    
    carry = '0'
    while index < max(len(a), len(b)) or carry == '1':
        num_a = a[-1 - index] if index < len(a) else '0'
        num_b = b[-1 - index] if index < len(b) else '0'
        
        val = self.to_int(num_a) + self.to_int(num_b) + self.to_int(carry)
        result = "%s%s" % (val % 2, result)
        
        carry = '1' if val > 1 else '0'
        index += 1

    return result

def to_int(self, c):
    if c == '1':
        return 1
    elif c == '0':
        return 0
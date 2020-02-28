#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 17:11:20 2018

@author: fubao
"""

# 273. Integer to English Words

# facebook

'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be
# less than 2^31 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

'''

'''
One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve \
              Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'
              
Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'
           
'Hundred' 

'Thousand', 'Million', 'Billion'

0 =>  zero

<= 19:  why 19  not 9

<= 100,   12  =>  1, 2
<= 1000,  312 =>  3,  12 =>  3,1,2

  < 10,000, 100,000, 1000,000 =>  all xx thousand
<= 1000, 000   xx thousand,  456,312 => 456  312       %1000
<= 1000,000,000,  xx million                  %1000,000
'''
class Solution(object):
    
    # 1st recursive version 
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve \
              Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        def words(n):
            if n < 20:
                return to19[n-1:n]
            if n < 100:
                return [tens[n/10-2]] + words(n%10)
            if n < 1000:
                return [to19[n/100-1]] + ['Hundred'] + words(n%100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000**(p+1):
                    return words(n/(1000**p)) + [w] + words(n%(1000**p))
        return ' '.join(words(num)) or 'Zero'
    
    
    # 2nd iterative version 
    def numberToWordsIterative(self, num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0:
        return 'Zero'
    ddict = {1: 'One', 2: 'Two', 3: "Three", 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
             10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15:'Fifteen', 16: 'Sixteen',
             17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
             60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
    base = ['', 'Thousand', 'Million', 'Billion']
    result, exp = '', 1000
    i, chunk = 0, 0
    while num:
        chunk = num % exp
        if chunk:
            result = base[i] + ' ' + result
            one = chunk % 10
            two = (chunk % 100) - one
            three = chunk // 100
            if two == 10:
                result = ddict[two+one] + ' ' + result
            else:
                if one:
                    result = ddict[one] + ' ' + result
                if two:
                    result = ddict[two] + ' ' +result
            if three:
                result = ddict[three] + ' Hundred ' + result
        num //= exp
        i += 1
    return result.rstrip()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 14:54:35 2018

@author: fubao
"""

'''

825. Friends Of Appropriate Ages

Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:

Input: [20,30,100,110,120]
Output: 
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
 

Notes:

1 <= ages.length <= 20000.
1 <= ages[i] <= 120.

'''


from collections import defaultdict

def numFriendRequests(ages):
    """
    :type ages: List[int]
    :rtype: int
    """
    
    def checkConditionTrue(ageA, ageB):
        '''
        age[B] <= 0.5 * age[A] + 7
        age[B] > age[A]
        age[B] > 100 && age[A] < 100
        '''
        
        if ageB <= 0.5 * ageA + 7:
            return False
        if ageB > ageA:
            return False
        if ageB > 100 and ageA < 100:
            return False
        return True
    
    '''
    #1st method, naive method, traverse two loops
    ans = 0
    for i in range(0, len(ages)):
        for j in range(0, len(ages)):
            if i != j:
                if checkConditionTrue(ages[i], ages[j]):
                    ans += 1
    return ans
    '''
    
    '''
    #2nd; TLE  there are some repetitions, like [16,16];  checked twice; [11, 10, 11, 10], 11 vs 10 checked twice; Time limit again
    res=defaultdict(tuple)
    ans = 0
    for i in range(0, len(ages)):
        for j in range(0, len(ages)):
            if i != j:
                if res[(ages[i], ages[j])] == 1:
                       ans += 1
                else:
                    if checkConditionTrue(ages[i], ages[j]):
                        res[(ages[i], ages[j])] = 1
                        ans += 1
    return ans                    
    '''
    
    # SUCCESS consider the number of ages;  age and count.   if age are the same, calculate the number 
    # [10, 3];          [11, 3] vs [12, 4]
    cr = defaultdict(int)
    # collections.Counter
    for a in ages:
        cr[a] += 1
    
    ans = 0
    #print("len cr: ", len(cr), type(cr), cr)
    for a, va in cr.items():
        for b, vb in cr.items():
            if a == b:
                if checkConditionTrue(a, b):
                    ans += va * (va-1)
            else:
                if checkConditionTrue(a, b):
                    ans += va * vb
    return ans
        
        
ages = [16, 16]
numFriendRequests(ages)

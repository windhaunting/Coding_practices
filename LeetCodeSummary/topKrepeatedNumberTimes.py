#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 19:09:15 2018

@author: fubao
"""

# repeated number

#given a (streaming) data size m, and a frequency k,  find the numbers of a word occurs m/k times.



# applications:

'''
1.popluar products: frequent viewed items
2.frequent search queries on Google
3. heavy TCP flows
4. volatile stocks 
...

# also reference : Top K Frequent Items Algorithm

http://zpjiang.me/2017/11/13/top-k-elementes-system-design/

'''

#if all data can be put in the memory;



# if its streaming, big data:
#  use count-min sketch data structure and heavy hitter problem learned in data science algorithm
'''
if k = 2,  that's find the numbers that occur > m/2 times:

    that is to find the majority element (in linear time)
    
     o(m) time, o(1) space   

Pseudo code:
    
    Input Array A:
    output: num
    
    Set count = 1,  current = A(1)
    for i = 2, 3, ...
        if count == 0: 
            set current = A(i)
            count = 1
        if A(i) == current,
            set count += 1
        else:
            set count -= 1
    return current
    
    
'''

'''
First talk about Count-Min:
    
    
The CM sketch is simply an array of counters of width w and depth d, CM[1, 1] . . . CM[d, w]. 
Each entry of the array is initially zero.
 Additionally, d hash functions
h1 . . . hd : {1 . . . n} → {1 . . . w}

are chosen uniformly at random from a pairwise-independent family. 
Once w and d are chosen, the space required is fixed:
the data structure is represented by wd counters and d hash functions (which can each be represented in O(1) machine
words.

Consider a vector a, which is presented in an implicit, incremental fashion (this abstract model
captures a wide variety of data stream settings, see entries on Data Stream Models for more details).
 This vector has dimension n, and its current state at time t is a(t) = [a1(t), . . . ai(t), . . . an(t)]. 
 
Initially, a(0) is the zero vector, 0, so a_i(0) is 0 for all i. Updates to individual entries of
 the vector are presented as a stream of pairs. The t^th update is (it, ct),
 meaning that
a_i(t) = a_i(t-1) + c_t

'''












'''
note:
    
if we want to estimate each number's frequency, which is point query problem, not heavy hitter,
for element i in A, estimate frequency f_i;  

'''
  
# if we 
# extension to moment



    

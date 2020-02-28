#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 18:13:06 2018

@author: fubao
"""

#  [Leetcode] Alien Dictionary

'''
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
Example 1:
Given the following words in dictionary,
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".
Example 2:
Given the following words in dictionary,
[
  "z",
  "x"
]
The correct order is: "zx".
Example 3:
Given the following words in dictionary,
[
  "z",
  "x",
  "z"
]
The order is invalid, so return "".
Note:
You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.

'''
from collections import defaultdict

class Solution(object):
    
    def __init__(self):
        self.inDegree = defaultdict(set) 
        self.outDegree = defaultdict(set) 

        self.vertices = set()
    
    def alienOrder(self, words):
        
        # first compare two  word's haracter one by one, iterate two loops
        #then set up the graph with the character
        
        # t-> f  w->e  r->t,  e->r
        
        # construct the indegree for each node
        for i in range(0, len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            for j in range(0, min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    self.inDegree[w2[j]].add(w1[j])
                    self.outDegree[w1[j]].add(w2[j])
                
                self.vertices.add(w1[j])
                self.vertices.add(w2[j])
         
        # use queue and indegree to get the topological order
        print ("vertices: ", self.vertices, self.inDegree, self.outDegree)
        que = []
        for v in self.vertices:
            if len(self.inDegree[v]) == 0:
                que.append(v)
        
        print ("queue: ", que)

        resOrder = []
        cnt = 0
        while (que):
            #pop
            u = que.pop(0)
            resOrder.append(u)
            
            # update the u's neighbor's indegree number
            for v in self.outDegree[u]:
                self.inDegree[v].remove(u)
                if len(self.inDegree[v]) == 0:
                    que.append(v)
        
            cnt += 1
        
        return resOrder
    
SolutionObj = Solution()
'''
words = ["wrt", "wrf", "er", "ett", "rftt"]
print (SolutionObj.alienOrder(words))

words = ["z", "f"]
print (SolutionObj.alienOrder(words))
'''
words = ["z", "x", "z"]
print (SolutionObj.alienOrder(words))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 17:15:56 2018

@author: fubao
"""

'''
union-find


A disjoint-set data structure is a data structure that keeps track of a set of elements
 partitioned into a number of disjoint (non-overlapping) subsets.
 A union-find algorithm is an algorithm that performs two useful operations on such a data structure:
    
application 1 :  Detect Cycle in an Undirected Graph;  like leetcode  to check Valid Tree


Find: Determine which subset a particular element is in. 
This can be used for determining if two elements are in the same subset.

Union: Join two subsets into a single subset.

'''



# https://www.geeksforgeeks.org/union-find/

from collections import defaultdict
  
#This class represents a undirected graph using adjacency list representation
class Graph:
  
    def __init__(self):
        self.V= set()    # store the vertices
        self.graph = defaultdict(list) # default dictionary to store graph
  
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.V.add(u)
        self.V.add(v)
        
    def union(self, parentArr, a, b):     # not path compression
        '''
        union a, b
        '''
        pa = self.findParent(parentArr, a)
        pb = self.findParent(parentArr, b)
        parentArr[pa] = pb
            
        
    def findParent(self, parentArr, a):
        '''
        find parent of an element a;     like the root of a tree
        '''
        if parentArr[a] != a:
            parentArr[a] = self.findParent(parentArr, parentArr[a])
        return parentArr[a]
        
        
    def checkCycle(self):
        '''
        check self.graph has cycle or not
        '''
        
        parentArr = [i for i in range(0, len(self.V))]
        
        for i in self.graph:
            for j in self.graph[i]:
                pi = self.findParent(parentArr, i)
                pj = self.findParent(parentArr, j)
                if pi == pj:
                    return True
                self.union(parentArr, pi, pj)
        return False
        
g = Graph()
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(1, 3)

print ("cycle or not ", g.checkCycle())




# 2nd optimized implementation

#  https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/

# previous union could be o(n) time;  if we optimize to o(logn) time

"""
%   http://joshuablog.herokuapp.com/Union-Find%E6%80%BB%E7%BB%93.html


305. Number of Islands II
在上一题的基础上，需要满足操作add，然后得出isolate的岛屿。
这道题需要建一个Union的类，这样每次调用类的操作能更好的减少时间空间复杂度，这次因为是需要在每次Add操作（isolate岛屿数量预先 count+1）的时候算出isolate的数量，所以可以对于每个新加入的点，向四周move一步，判断是否和已知岛屿联通，从而count-1

class Solution(object):
    def numIslands2(self, m, n, positions):
        ans = []
        islands = Union()
        for p in map(tuple, positions):
            islands.add(p)
            for dp in (0, 1), (0, -1), (1, 0), (-1, 0):
                q = (p[0] + dp[0], p[1] + dp[1])
                if q in islands.group:
                    islands.union(p, q)
            ans += [islands.count]
        return ans

class Union(object):
    def __init__(self):
        self.group = {}
        self.island = {}
        self.count = 0

    def add(self, p):
        self.group[p] = p
        self.island[p] = 1
        self.count += 1

    def find(self, i):
        if i == self.group[i]:
            return i
        else:
            return self.find(self.group[i])

    def union(self, p, q):
        root1, root2 = self.find(p), self.find(q)
        if root1 == root2:
            return
        if self.island[root1] > self.island[root2]:
            root1, root2 = root2, root1
        self.group[root1] = root2
        self.island[root2] += self.island[root1]
        self.count -= 1
"""
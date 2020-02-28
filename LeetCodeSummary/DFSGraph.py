#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 20:10:55 2018

@author: fubao
"""

#  DFS Depth First Traversal  for graph


#1st  recursive way
# 2nd iterative way

from collections import defaultdict
 
#Class to represent a graph
class Graph:
    def __init__(self):
        self.graph = defaultdict(list) # dictionary containing adjacency List
        self.vertices = set() # vertices
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        if u not in self.vertices:
            self.vertices.add(u)
        if v not in self.vertices:
            self.vertices.add(v)
            
            
    def dfsRecursive(self, src):
        '''
        recursive dfs
        '''
        visited = [False] * (len(self.vertices))
        self.dfsHelper(src, visited)
            
                    
    def dfsHelper(self, v, visited):
        # visited
        visited[v] = True
        print ("v: ", v)
        
        for n in self.graph[v]:
            if visited[n] == False:
                self.dfsHelper(n, visited)
                
     
        
    #2nd dfs iterative research    
    def dfsIterative(self, src):
        '''
        iterative traversal dfs with stack
        '''
        visited = [False] * (len(self.graph))
        
        stk = []   # stack
        stk.append(src)
        visited[src] = True
        
        while (len(stk)):
            v = stk.pop()       # last element
            print ("visited: ", v)

            for n in self.graph[v]:
                if not visited[n]:
                    stk.append(n)
                    visited[n] = True
        
        
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is DFS recursive from (starting from vertex 2)", g.dfsRecursive(2))
print ("Following is DFS iterative from (starting from vertex 2)", g.dfsIterative(2))





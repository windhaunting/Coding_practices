#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 22:12:38 2018

@author: fubao
"""

# BFS  Breadth first search

# use iterative way

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
            
            
        
    def bfsIterative(self, src):
        '''
        iterative traversal dfs with stack
        '''
        visited = [False] * (len(self.graph))
        
        que = []   # stack
        que.append(src)
        visited[src] = True
        
        while (len(que)):
            v = que.pop(0)       # last element
            print ("visited: ", v)
            for n in self.graph[v]:
                if not visited[n]:
                    que.append(n)
                    visited[n] = True
        
        
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
 
print ("Following is bfs iterative from (starting from vertex 2)", g.bfsIterative(2))


# bidirectional bfs, here we have two sources, so the common improved way is to use bidirectional bfs?


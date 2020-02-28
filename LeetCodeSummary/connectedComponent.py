#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 16:55:57 2018

@author: fubao
"""

# connected component  ;  check a graph how many connected component



# reference:
#https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/



'''
We have discussed algorithms for finding strongly connected components 
in directed graphs in following posts.
Kosaraju’s algorithm for strongly connected components.
Tarjan’s Algorithm to find Strongly Connected Components

Finding connected components for an undirected graph is an easier task. We simple need to do either BFS or DFS starting from every unvisited vertex, and we get all strongly connected components. Below are steps based on DFS.

1) Initialize all vertices as not visited.
2) Do following for every vertex 'v'.
       (a) If 'v' is not visited before, call DFSUtil(v)
       (b) Print new line character

DFSUtil(v)
1) Mark 'v' as visited.
2) Print 'v'
3) Do following for every adjacent 'u' of 'v'.
     If 'u' is not visited, then recursively call DFSUtil(u)
     
'''

from collections import defaultdict
 
#Class to represent a graph
class Graph:
    def __init__(self):
        self.graph = defaultdict(list) # dictionary containing adjacency List
        self.vertices = set() # vertices
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

        if u not in self.vertices:
            self.vertices.add(u)
        if v not in self.vertices:
            self.vertices.add(v)
            
            
    def connectedComponents(self):
        '''
        recursive dfs
        '''
        
        visited = [False] * (len(self.vertices))
        cnt = 0
        for src in self.vertices:

            if not visited[src]:
                self.dfsHelper(src, visited)
                print ("\n")
                cnt += 1
        print ("cnt: ", cnt)

                    
    def dfsHelper(self, v, visited):
        # visited
        visited[v] = True
        print ("v: ", v)
        
        for n in self.graph[v]:  # neighbors
            if visited[n] == False:
                self.dfsHelper(n, visited)
                
                
            

g = Graph(); # 5 vertices numbered from 0 to 4
g.addEdge(1, 0)
g.addEdge(2, 3)
g.addEdge(3, 4)
 
print("Following are connected components \n")
g.connectedComponents()


#2nd  use union-find method
Number of Connected Components in an Undirected Graph
# https://zhuhan0.blogspot.com/2017/03/leetcode-323-number-of-connected.html

def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def find(x):
        	if uf[x] != x:
        		uf[x] = find(uf[x])
        	return uf[x]

        def union(x,y):
        	xRoot = find(x)
        	yRoot = find(y)
        	uf[xRoot] = yRoot

        uf = [i for i in range(n)]

        for node1, node2 in edges:
        	union(node1, node2)

        res = set()
        for i in range(n):
        	res.add(find(i))

        return len(res)

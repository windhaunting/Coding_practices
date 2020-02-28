#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 15:31:19 2018

@author: fubao
"""

#   Depth First Search ; DFS


# Python program to print DFS traversal from a
# given given graph
from collections import defaultdict
 
# This class represents a directed graph using
# adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # A function used by DFS
    def DFSUtil(self,v,visited):
 
        # Mark the current node as visited and print it
        visited[v]= True
        print (v)
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
 
 
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self,v):
 
        # Mark all the vertices as not visited
        visited = [False]*(len(self.graph))
 
        # Call the recursive helper function to print
        # DFS traversal
        self.DFSUtil(v,visited)
        
    # use iterative way ;  adjacency list
    
    def dfs_iterative(graph, start):
        stack, path = [start], []
    
        while stack:
            vertex = stack.pop()
            if vertex in path:
                continue
            path.append(vertex)
            for neighbor in graph[vertex]:
                stack.append(neighbor)
    
        return path
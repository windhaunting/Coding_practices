#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 10:20:48 2018

@author: fubao
"""

# check cycle


# application 
# leetcode Graph Valid Tree


#1st  Detect Cycle in a Directed Graph

'''
Given a directed graph, 
check whether the graph contains a cycle or not. 
Your function should return true if the given graph 
contains at least one cycle, else return false.
 For example, the following graph contains three cycles 0->2->0, 0->1->2->0 and 3->3, 
 so your function must return true.

a disconnected graph, we get the DFS forrest as output. 
To detect cycle, we can check for cycle in individual trees by checking back edges.

'''

# Python program to detect cycle 
# in a directed graph

# Time Complexity of this method is same as time complexity of DFS traversal which is O(V+E)

from collections import defaultdict
 
class Graph1():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def isCyclicUtil(self, v, visited, recStack):
 
        # Mark current node as visited and 
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
 
        # Recur for all neighbours
        # if any neighbour is visited and in 
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 
        # The node needs to be poped from 
        # recursion stack before function ends
        recStack[v] = False
        return False
 
    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False
 

g = Graph1(6)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
#g.addEdge(2, 0)
#g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(5, 3)

if g.isCyclic() == 1:
    print ("Directed Graph has a cycle")
else:
    print ("Directed Graph has no cycle")
    


#2nd undirected graph 
# (1) use DFS traversal too
# (2) use union-find method,  time complexity of the union-find algorithm is O(ELogV)
    
'''
(1) DFS: 
     do a DFS traversal of the given graph.
     For every visited vertex ‘v’, if there is an adjacent ‘u’ such that u is already visited and
     u is not parent of v, then there is a cycle in graph. 
     If we don’t find such an adjacent for any vertex, we say that
     there is no cycle. The assumption of this approach is that 
     there are no parallel edges between any two vertices
'''
         

# Python Program to detect cycle in an undirected graph
 
from collections import defaultdict
  
#This class represents a undirected graph using adjacency list representation
class Graph2:
  
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
 
  
    # function to add an edge to graph
    def addEdge(self,v,w):
        self.graph[v].append(w) #Add w to v_s list
        self.graph[w].append(v) #Add v to w_s list
  
    # A recursive function that uses visited[] and parent to detect
    # cycle in subgraph reachable from vertex v.
    def isCyclicUtil(self,v,visited,parent):
 
        #Mark the current node as visited 
        visited[v]= True
 
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            # If the node is not visited then recurse on it
            if  visited[i]==False : 
                if(self.isCyclicUtil(i,visited,v)):
                    return True
            # If an adjacent vertex is visited and not parent of current vertex,
            # then there is a cycle
            elif  parent!=i:
                return True
         
        return False
         
  
    #Returns true if the graph contains a cycle, else false.
    def isCyclic(self):
        # Mark all the vertices as not visited
        visited =[False]*(self.V)
        # Call the recursive helper function to detect cycle in different
        #DFS trees
        for i in range(self.V):
            if visited[i] ==False: #Don't recur for u if it is already visited
                if(self.isCyclicUtil(i,visited,-1))== True:
                    return True
         
        return False
 
# Create a graph given in the above diagram
g = Graph2(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
 
if g.isCyclic():
    print ("undirected Graph contains cycle")
else :
    print ("undirected Graph does not contain cycle ")
    
g1 = Graph2(3)
g1.addEdge(0,1)
g1.addEdge(1,2)
 
if g1.isCyclic():
    print ("undirected Graph contains cycle")
else :
    print ("undirected Graph does not contain cycle ")
  
       
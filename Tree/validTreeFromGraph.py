#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 15:09:01 2018

@author: fubao
"""

 

#  Graph Valid Tree | LeetCode   facebook


'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Hint:

Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree?
According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.


'''




# reference:

# https://discuss.leetcode.com/topic/21737/8-10-lines-union-find-dfs-and-bfs/2

# normal way of BFS:
# The input edges are meant for directed graph, so first we need to cover it to the input for undirected graph.

def validTree(self, n, edges):
    dic = {i: set() for i in xrange(n)}        # adjacency list
    for i, j in edges:
        dic[i].add(j)
        dic[j].add(i)
    visited = set()
    queue = collections.deque([dic.keys()[0]])
    while queue:
        node = queue.popleft()
        if node in visited:
            return False
        visited.add(node)
        for neighbour in dic[node]:
            queue.append(neighbour)
            dic[neighbour].remove(node)
        dic.pop(node)
    return not dic


'''
Solution 1 ... Union-Find

The test cases are small and harmless, simple union-find suffices (runs in about 50~60 ms).

def validTree(self, n, edges):
    parent = range(n)
    def find(x):
        return x if parent[x] == x else find(parent[x])
    def union(xy):
        x, y = map(find, xy)
        parent[x] = y
        return x != y
    return len(edges) == n-1 and all(map(union, edges))
A version without using all(...), to be closer to other programming languages:

def validTree(self, n, edges):
    parent = range(n)
    def find(x):
        return x if parent[x] == x else find(parent[x])
    for e in edges:
        x, y = map(find, e)
        if x == y:
            return False
        parent[x] = y
    return len(edges) == n - 1
A version checking len(edges) != n - 1 first, as parent = range(n) could fail for huge n:

def validTree(self, n, edges):
    if len(edges) != n - 1:
        return False
    parent = range(n)
    def find(x):
        return x if parent[x] == x else find(parent[x])
    def union(xy):
        x, y = map(find, xy)
        parent[x] = y
        return x != y
    return all(map(union, edges))
    
    
    
    
Solution 2 ... DFS

def validTree(self, n, edges):
    neighbors = {i: [] for i in range(n)}
    for v, w in edges:
        neighbors[v] += w,
        neighbors[w] += v,
    def visit(v):
        map(visit, neighbors.pop(v, []))
    visit(0)
    return len(edges) == n-1 and not neighbors
Or check the number of edges first, to be faster and to survive unreasonably huge n:

def validTree(self, n, edges):
    if len(edges) != n - 1:
        return False
    neighbors = {i: [] for i in range(n)}
    for v, w in edges:
        neighbors[v] += w,
        neighbors[w] += v,
    def visit(v):
        map(visit, neighbors.pop(v, []))
    visit(0)
    return not neighbors
For an iterative version, just replace the three "visit" lines with

    stack = [0]
    while stack:
        stack += neighbors.pop(stack.pop(), [])
Solution 3 ... BFS

Just like DFS above, but replace the three "visit" lines with

    queue = [0]
    for v in queue:
        queue += neighbors.pop(v, [])
or, since that is not guaranteed to work, the safer

    queue = collections.deque([0])
    while queue:
        queue.extend(neighbors.pop(queue.popleft(), []))
        
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:53:11 2018

@author: fubao
"""

# 310. Minimum Height Trees

'''
For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
'''



from collections import defaultdict
from collections import OrderedDict
import operator

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        
        # 1st naive way to set each node as root, and then try to get its longest height 
        
        '''
        #2st optimize naive way; set a node that has largest to smallest degrees to start over first; during each tree's traversing, compare with the current height and decide to stop the traversing or not (no need to traverse the deepest leaf node to find its tree height ? ) 
        
        if n == 0:
            return []
        elif edges is None or edges == []:
            return [0]
        
        dic = defaultdict(list)
        for (i, j) in edges:
            dic[i].append(j)
            dic[j].append(i)
        
        # sort according to list length
        dic = OrderedDict(sorted(dic.items(), key=lambda x: x[1]))
        #print ("dic: ", type(dic), dic )
        
        ansLst = []
        maxTreeHeight = 2**32
        for k in dic.keys():
            #k as a root
            # get tree height 
            visited = []
            que = [k]
            treeHeight = 0
            while(len(que)):
                # pop que
                l = len(que)
                while(l > 0):
                    cur = que.pop(0)
                    l -= 1
                    if cur  in visited:
                        continue
                    visited.append(cur) 
                    for nb in dic[cur]:
                        que.append(nb)
                treeHeight += 1
                if treeHeight > maxTreeHeight:
                    break
            
            #print ("k: ", k, treeHeight)
            if treeHeight == maxTreeHeight:
                ansLst.append(k)
            elif treeHeight < maxTreeHeight:
                maxTreeHeight = treeHeight
                ansLst.clear()
                ansLst.append(k)
        
        return ansLst
        '''
        
        #3rd consider the special characteristics;  only maximum one or two nodes could be the final node number; get each node's degree;
        #if node's degree is 0 add them all into a list;       # 1-0-2       []; 0; 0-1;  0-1-2;  0-1-2-3; 0-1-2-3-4; 
        if n == 0:
            return []
        elif edges is None or edges == []:
            return [0]
        
        degOneLst = []
        dic = defaultdict(list)
        dicDeg = defaultdict(int)
        for (i, j) in edges:
            dic[i].append(j)
            dic[j].append(i)
            dicDeg[i] += 1
            dicDeg[j] += 1
            
        for k, v in dic.items():
            if len(v) == 1:
                degOneLst.append(k)
            
        #print ("dicDeg: ", dicDeg, dic, degOneLst)
        
        ansLst = []
        
        while(len(degOneLst)): 
            ln = len(degOneLst)
            ansLst = degOneLst[::]
            #print ("degOneLst: ", degOneLst, ansLst)
            while(ln > 0):
                nd = degOneLst.pop(0)
                #ansLst.append(nd)
                #dicDeg.pop(nd, None)
                del dicDeg[nd]
                for neigb in dic[nd]:          # should be only one neigb element; because degree is one; no need to use for loop in reality
                    dicDeg[neigb] -= 1
                    if dicDeg[neigb] == 1:     # add to degOneLst
                        degOneLst.append(neigb)
                        
                del dic[nd]
                ln -= 1    
            
        return ansLst
        
        
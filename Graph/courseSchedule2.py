#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 08:58:00 2018

@author: fubao
"""



# 210. Course Schedule II

'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''

#topological sort


# refer the topological sort in the Leetcode summary

from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # this problem is actully topological sort when consider the input as garaph;;
        # get the order of topological sorting
        
        # get the edge list
        graph = defaultdict(list)  
        #get the indegree of each element(node)
        indeg = defaultdict(int)        # indegree dictionary
        for ls in prerequisites:
            graph[ls[1]].append(ls[0])
            indeg[ls[1]] += 1
        

        que = []      #queue
        for u in range(0, numCourses):     # numCourses, not  indeg
            if indeg[u] == 0:
                que.append(u)
                
        ans = []
        
        cnt = 0
        while (que):
            
            # pop from que
            u = que.pop(0)
            ans.append(u)
            
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    que.append(v)
            cnt += 1
        
        if cnt != numCourses:
            print ("there is a cycle in the graph; no possbile way to achieve this")
            return []
        else:
            print (ans)
            
        return ans
            
    
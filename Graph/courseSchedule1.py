#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:09:46 2019

@author: fubao
"""

# facebook  course schedule I

'''
207. Course Schedule
Medium
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
             
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #FAILURE OF WRITING ITERATIVELY idea 1: modeal a graph and check if there's a cycle in the graph
        # edge list
        # how to check a cycle, use dfs or union-find 
        if not prerequisites or len(prerequisites) == 0:
            return True
        
        from collections import defaultdict
        dict_graph = defaultdict(list)
        for eg in prerequisites:
            dict_graph[eg[0]] += [eg[1]]
            
        dict_graph_cp = dict_graph.copy()
        for n, nb in dict_graph.items():
            # dfs check cycle
            cycleFlag = self.hasCycle(dict_graph_cp, n)
            print ("len cycleFlag: ", n,  cycleFlag)
            if cycleFlag:
                return False
        return True
            
    def hasCycle(self, dict_graph, n):
        # use DFS
        stk = [n]
        lst_visited = set()
        while (len(stk)):
            #pop 
            nd = stk.pop(-1)
            lst_visited.add(nd)

            for nb in dict_graph[nd]:
                if nb in lst_visited:       # FAILURE FOR CASE 3
[[0,1],[0,2],[1,2]]
                    return True
                else:
                    stk.append(nb)
                    
            #print ("len stk: ", stk)
        return False
    
            '''
        #SUCCESS idea 2 use DFS recursive way to decide a cycle
        from collections import defaultdict
        dict_graph = defaultdict(list)
        for eg in prerequisites:
            dict_graph[eg[0]] += [eg[1]]

        visited = [False]*numCourses
        recurStk = [False]*numCourses
        dict_graph_cp = dict_graph.copy()
        for n, nb in dict_graph.items():
            # dfs check cycle
            if not visited[n]:
                if self.hasCycle(dict_graph_cp, n, visited, recurStk):
                    #print ("len cycleFlag: ", n )
                    return False
        return True
    
    
    def hasCycle(self, dict_graph, n, visited, recurStk):
        
        visited[n] = True
        recurStk[n] = True
        for nb in dict_graph[n]:
            if not visited[nb]:
                 if self.hasCycle(dict_graph, nb, visited, recurStk):
                        return True
            elif recurStk[nb]:
                return True
        recurStk[n] = False
        return False
        '''
    
    #3rd using topological sort BFS get the indegree, get each node's indegree, then use topological sort from a node with indegree == 0
    # if we can not visit all the node, there exists a cycle in the graph
        if not prerequisites or len(prerequisites) == 0:
            return True
        
        from collections import defaultdict
        dict_graph = defaultdict(list)
        dict_indeg = defaultdict(int)
        for eg in prerequisites:
            dict_graph[eg[0]] += [eg[1]]
            dict_indeg[eg[1]] += 1
            
        que = []
        for nd in range(0, numCourses):
            if dict_indeg[nd] == 0:
                que.append(nd)
        cnt = 0  
        #print ("que: ", que, dict_indeg)
        while (len(que)):
            nd = que.pop(0)
            
            cnt += 1
            for nb in dict_graph[nd]:
                dict_indeg[nb] -= 1
                if dict_indeg[nb] == 0:
                    que.append(nb)
            #print ("nd: ", nd)
        if cnt != numCourses:  # there is a cycle
            return False
        return True
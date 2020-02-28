#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:48:38 2018

@author: fubao
"""



# https://www.geeksforgeeks.org/backttracking-set-5-m-coloring-problem/


isValidBipartiteGraph 

'''
One approach is to check whether the graph is 2-colorable or not using backtracking algorithm m coloring problem.

Following is a simple algorithm to find out whether a given graph is Birpartite or not using Breadth First Search (BFS).
1. Assign RED color to the source vertex (putting into set U).
2. Color all the neighbors with BLUE color (putting into set V).
3. Color all neighbor’s neighbor with RED color (putting into set U).
4. This way, assign color to all vertices such that it satisfies all the constraints of m way coloring problem where m = 2.
5. While assigning colors, if we find a neighbor which is colored with same color as current vertex, 
then the graph cannot be colored with 2 vertices (or graph is not Bipartite)


'''


# reference: http://www.cnblogs.com/EdwardLiu/p/6552027.html

 #  Java Code
 3 import java.util.*;
 4 
 5 public class Bipartite {
 6     HashSet<Integer> list1 = new HashSet<Integer>();
 7     HashSet<Integer> list2 = new HashSet<Integer>();
 8     
 9     public void bfs(int[][] relations) {
10         HashMap<Integer, HashSet<Integer>> graph = new HashMap<Integer, HashSet<Integer>>();
11         for (int[] each : relations) {
12             if (!graph.containsKey(each[0]))
13                 graph.put(each[0], new HashSet<Integer>());
14             if (!graph.containsKey(each[1]))
15                 graph.put(each[1], new HashSet<Integer>());
16             graph.get(each[0]).add(each[1]);
17             graph.get(each[1]).add(each[0]);
18         }
19         
20         
21         Queue<Integer> queue = new LinkedList<Integer>();
22         queue.offer(relations[0][0]);
23         list1.add(relations[0][0]);
24         HashSet<Integer> visited = new HashSet<Integer>();
25         visited.add(relations[0][0]);
26         int count = 1;
27         while (!queue.isEmpty()) {
28             int size = queue.size();
29             for (int i=0; i<size; i++) {
30                 int person = queue.poll();
31                 HashSet<Integer> friends = graph.get(person);
32                 for (int each : friends) {
33                     if (list1.contains(each)&&list1.contains(person) || list2.contains(each)&&list2.contains(person)) {
34                         list1.clear();
35                         list2.clear();
36                         return;
37                     }
38                         
39                     if (!visited.contains(each)) {
40                         if (count%2 == 1) list2.add(each);
41                         else list1.add(each);
42                         queue.offer(each);
43                         visited.add(each);
44                     }
45                 }
46             }
47             count++;
48         }
49     }


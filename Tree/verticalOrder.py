#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 01:08:32 2018

@author: fubao
"""

#print a binary tree in vertical order;  facebook


# 314 Binary Tree Vertical Order Traversal 
'''
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
 

return its vertical order traversal as:

[
  [9],
  [3,15],
  [20],
  [7]
]
 

Given binary tree [3,9,20,4,5,2,7],

    _3_
   /   \
  9    20
 / \   / \
4   5 2   7
 

return its vertical order traversal as:

[
  [4],
  [9],
  [3,5,2],
  [20],
  [7]
]
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

 
class Solution(object):
    
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        
        use level order traversal and hashmap to store/record the distance of each node from the root
        """
        
        if not root:
            return []
        nodeDistMap = {}
        #\ level traveral use queue  FIFO
        que = [(root, 0)]
        minDist = 0  # 2**32
        maxDist =  0 #-1*(2**32)
        
        result = []
        while (len(que) != 0):
            #deque from que
            node, dist = que.pop(0)
            if dist not in nodeDistMap:
                nodeDistMap[dist] = [node.val]
            else:
                nodeDistMap[dist].append(node.val)
            #add left and right node into queue
            if node.left:
                minDist = min(minDist, dist-1)
                que.append((node.left,  dist-1))
            if node.right:
                maxDist = max(maxDist, dist+1)
                que.append((node.right, dist+1))
            
        for i in range(minDist, maxDist):
            result.append(nodeDistMap[i])
        
        return result
            
            
            

        
        
        
        
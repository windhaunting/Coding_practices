#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:26:32 2019

@author: fubao
"""



# facebook 

'''
199. Binary Tree Right Side View
Medium

1330

71

Favorite

Share
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        # idea 1: Failed use recursive way, check right children nodes.
        # if there is no right node, check it's left children node
        # problem with case [1,2,3,4],
        if root is None:
            return None
        res = []
        self.rightViewHelper(root, res)
    
        return res
    
    def rightViewHelper(self, nd, res):
        if nd is None:
            return
        res.append(nd.val)
        
        if nd.right is not None:
            self.rightViewHelper(nd.right, res)
            
        else:
            self.rightViewHelper(nd.left, res)
            
        '''    
        #SUCCESS 2nd idea is use BFS , output each level's node and get the last element in each level
        #no need to store in the list and then visit [-1]
        # overwrite the depth (level)
        '''
        if root is None:
            return None
        que = [(root, 0)]
        dict_res = defaultdict()
        max_dep = 0
        while (len(que)):
            nd, dep = que.pop(0)
            
            max_dep = max(dep, max_dep)
            dict_res[dep] = nd.val
            
            if nd.left:
                que.append((nd.left, dep+1))
            if nd.right:
                que.append((nd.right, dep+1))
        
        return [dict_res[i] for i in range(0, max_dep+1)]
        '''
    
        # SUCCESS 3rd idea use DFS # also search using each node, and each layer's first visited node is  the node is the node viewed from right side at each layer. 
        if root is None:
            return None
        stk = [(root, 0)]
        
        dict_res = {}
        max_dep = 0
        while(len(stk)):
            nd, dep = stk.pop(-1)
            
            max_dep = max(dep, max_dep)
            
            if dep not in dict_res:
                dict_res[dep] = nd.val
            if nd.left:
                stk.append((nd.left, dep+1))
            if nd.right:
                stk.append((nd.right, dep+1))
        
        return [dict_res[i] for i in range(0, max_dep+1)]
        
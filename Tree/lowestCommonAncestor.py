#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 23:46:28 2018

@author: fubao
"""

# 236. Lowest Common Ancestor of a Binary Tree

'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        '''
        #1st use BFS traversal, record each nodes' parents in a list
        #if p is in q's parent list, then p is LCA, vice versa,...
        '''
        '''
        if root is None:
            return None
        que = [(root, [root])]   # queue
        pLst = []
        qLst = []
        pFlag = False;
        qFlag = False
        while (len(que)):
            # pop 
            nodeInfo = que.pop(0)
            nd = nodeInfo[0]
            valLst = nodeInfo[1]
            #print ("valLst: ", nd.val,p.val,q.val, pLst, qLst, valLst)
            if nd == p:
                pLst = valLst
                pFlag = True
            if nd == q:
                qLst = valLst
                qFlag = True
            if pFlag and qFlag:
                break
            if nd.left is not None:
                que.append((nd.left, [nd.left] + valLst))
            if nd.right is not None:
                que.append((nd.right, [nd.right] + valLst))
      
        #print ("p, q: ", pLst, qLst)
        l = 0
        r = 0
        while (l < len(pLst)):
            r = 0
            while (r < len(qLst)):
                #print ("aap: ", pLst[l], qLst[r])
                if pLst[l] == qLst[r]:
                    return pLst[l]
                r+=1
            l+=1
            
        return None
    
        '''
        #2nd use hashmap to save memory
        
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q
        

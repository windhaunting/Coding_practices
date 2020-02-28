#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 19:01:59 2018

@author: fubao
"""



# 100. Same Tree

'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.


Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        #1st recursive way iteration
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        
        '''
        #2nd iterative way DFS to two trees
        stp = []
        stq = []
        if p is None and  q is None:
            return True
        stp.append(p)
        stq.append(q)
        while (len(stp) or len(stq)):
            nodep = stp.pop()
            nodeq = stq.pop()
            #print ('nodep, nodeq : ', nodep, nodeq)

            if (nodep and not nodeq) or (nodeq and not nodep):
                return False
            elif nodep  and nodeq and nodep.val != nodeq.val:
                return False
            
            if nodep:
                stp.append(nodep.right)
                stp.append(nodep.left)
                
            if nodeq:
                stq.append(nodeq.right)
                stq.append(nodeq.left)
        return True
        '''    
            
            
            



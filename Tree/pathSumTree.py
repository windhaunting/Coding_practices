#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 10:43:55 2018

@author: fubao
"""


# 113. Path Sum II

'''
For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]


'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        
        # iterative use bfs to traversal to record the node and the path node value starting from its parent to itself while traversing
        '''
        if root is None:
            return []
        
        d = []
        s = sum
        innerLst = [root.val]
        ansLst = []
        d.append((root, innerLst))
        while (len(d)):
            nodeInfo = d.pop(0)
            node = nodeInfo[0]
            innerLst = nodeInfo[1]
            if not node.left and not node.right:
                #print ("innerLst: ", innerLst, s, type(innerLst))
                #sumPath = sum(innerLst)
                sumPath = 0
                for e in innerLst:
                    sumPath+=e
                if sumPath == s:
                    ansLst.append(innerLst)
            if node.left:
                d.append((node.left, innerLst + [node.left.val]))
            if node.right:
                d.append((node.right, innerLst + [node.right.val]))
        return ansLst
        '''
        
        # 2nd recursive way:
        
        if not root:
            return []
        res = []
        self.dfs(root, sum, [], res)
        return res

    def dfs(self, root, sum, curr, res):
        if not root.left and not root.right and sum == root.val:
            curr.append(root.val)
            res.append(curr)
        if root.left:
            self.dfs(root.left, sum-root.val, curr+[root.val], res)
        if root.right:
            self.dfs(root.right, sum-root.val, curr+[root.val], res)
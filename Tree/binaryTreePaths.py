#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:27:41 2018

@author: fubao
"""


# 257. Binary Tree Paths

'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        
        #dfs store path iterative 
        if root is None:
            return []
        resultsLst = []
        pathLst = []           #stack
        
        pathLst.append([root])
        while(len(pathLst)):
            #print ("pathLst ", pathLst)
            prevPath = pathLst.pop()
            #print ("prevPath ", prevPath)
            node = prevPath[-1]
            #print ("tt ", node.val)
            if node.left:
                t2 = prevPath[:]
                t2.append(node.left)
                pathLst.append(t2)
            
            if node.right:
                t1 = prevPath[:]
                t1.append(node.right)
                pathLst.append(t1)

            if node.right is None and node.left is None:           #arrive leaf node
                elem = ''
                for node in prevPath[0:len(prevPath)-1]: # or [:-1]?
                    elem += str(node.val) + '->'
                elem += str(prevPath[-1].val)
                resultsLst.append(elem)
        return resultsLst
        
        
        '''
        #2nd recursive
        resultLst = []
        if root:
           self.helperTraverse(root, "", resultLst)
        return resultLst
           
    def helperTraverse(self, root, path, resultLst):
        if root.left is None and root.right is None:
            resultLst.append(path + str(root.val))
        if root.left:
            self.helperTraverse(root.left, path + str(root.val) + "->", resultLst)
        if root.right:
            self.helperTraverse(root.right, path + str(root.val) + "->", resultLst)
        '''
        
        '''
        #3rd method using dfs recursive way, more clever from other guy
        if not root:
            return []
        resultLst = [str(root.val) + "->" + path for path in self.binaryTreePaths(root.left)]
        print ('aaaa  ', resultLst)
        resultLst +=[str(root.val) + "->" + path for path in self.binaryTreePaths(root.right)]
        print ('resultLst22  ', resultLst)
        return resultLst or [str(root.val)] 
        '''
        

    
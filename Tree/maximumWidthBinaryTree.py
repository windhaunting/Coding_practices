#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 14:39:54 2019

@author: fubao
"""

# https://leetcode.com/problems/maximum-width-of-binary-tree/


# 662. Maximum Width of Binary Tree


'''

662. Maximum Width of Binary Tree


Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#1ST FAILURE 1st use level order traversal. considering null node at each level and record each node in each level's visited list
# take too much spaces, not efficient

'''
class Solution:
    def widthOfBinaryTree(self, root: 'TreeNode') -> 'int':
         
        q = []
        
        q.append(root)
        maxLen = 0
        while(len(q)):
            
            n = len(q)
            levelLst = []
            while(n):
                # pop queue
                nd = q.pop(0)
                if nd is None and len(levelLst) != 0:
                    levelLst.append('#')
                elif nd is not None:
                    levelLst.append(nd.val)
                    
                if nd is None and len(levelLst) != 0:
                    q.append(None)
                    q.append(None)                    
                elif nd is not None:
                    if nd.left is None:
                        q.append(None)
                    else:
                        q.append(nd.left)

                    if nd.right is None:
                        q.append(None)
                    else:
                        q.append(nd.right)
                
                n -= 1
            maxLen = max(self.getLength(levelLst), maxLen)
            print ("maxLen: ", maxLen)
        
        return maxLen
            
    def getLength(self, levelLst):
        
        if len(levelLst) == 0:
            return 0
        begin = -1
        
        i = 0
        while (i < len(levelLst)):
            if levelLst[i] == '#':
                continue;
            else:
                begin = i
                break
            i += 1
            
        j = len(levelLst)-1 
        end = -1
        
        while (j >= 0):
            if levelLst[j] == '#':
                continue
            else:
                end = j
                break
            j -= 1
                
        return end-begin+1

'''
# https://leetcode.com/problems/maximum-width-of-binary-tree/solution/
#2nd use BFS, it's so easy, only record depth and position index of each node

class Solution:
    def widthOfBinaryTree(self, root: 'TreeNode') -> 'int':
         
        q = []
        q.append((root, 0, 0))
        curDep = 0
        left = 0
        maxW = 0     # max width
        while(len(q)):
            ndInfo = q.pop(0)
            nd = ndInfo[0]
            dep = ndInfo[1]
            indx = ndInfo[2]
            if nd.left is not None:
                q.append((nd.left, dep+1, 2*indx+1))
            if nd.right is not None:
                q.append((nd.right, dep+1, 2*indx+2))
            if curDep != dep:
                curDep = dep
                left = indx
            maxW = max(indx - left+1, maxW)
        return maxW


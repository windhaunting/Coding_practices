#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 08:39:46 2018

@author: fubao
"""




# tree BFS or DFS traversal;
# level traversal


'''
e.g.


 Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        '''
        # 1st SUCCESS use recursive  order traversal dfs 
        
        if root is None:
            return 0
        
        def getTreeDepthHelper(node, depth, res):
            if node.left is None and node.right is None:
                if depth > res[1]:
                    # update depth
                    res[0] = node
                    res[1] = depth
            if node.left is not None:
                getTreeDepthHelper(node.left, depth+1, res)
            if node.right is not None:
                getTreeDepthHelper(node.right, depth+1, res)
            #print ("res: ", depth, res[0].val)
        
        depth = 1
        res = [root, 1]
        getTreeDepthHelper(root, depth, res)
        return res[0].val
        '''
        
    

        #2nd  SUCCESS,  use iterative 
        
        res = [root, 1]
        que = [(root, 1)]
        while (len(que)):
            # pop
            ele = que.pop(0)
            node = ele[0]
            depth = ele[1]
            
            if depth > res[1]:
                #update
                res[0] = node
                res[1] = depth 
            if node.left is not None:
                que.append((node.left, depth+1))
            if node.right is not None:
                que.append((node.right, depth+1))
            
        return res[0].val
    
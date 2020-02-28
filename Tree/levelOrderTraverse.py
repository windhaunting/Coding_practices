#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 10:24:03 2018

@author: fubao
"""




#  102. Binary Tree Level Order Traversal -


'''

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]



'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        d = deque()
        d.append(root)
        resLst = []
        while(len(d)):
            n = len(d)
            lst = []
            while(n > 0):
                node = d.popleft()
                lst.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
                n -= 1
            resLst.append(lst)

        return resLst
        
    
    
    #2nd  use recursive way  DFS
        ans = []
        self.helper(root,0, ans) #no need to check root == None before helper()\
        return ans

    def helper(self,root,level, ans):
        if not root:
            return [] # instead of None
        else:
            if level<len(ans):
                ans[level].append(root.val)
            else:
                ans.append([root.val])
            self.helper(root.left,level+1, ans)
            self.helper(root.right,level+1, ans)
        #return ans
 
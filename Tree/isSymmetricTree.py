#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 18:32:45 2018

@author: fubao
"""




#  101. Symmetric Tree


'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.


'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        非递归解法：按层遍历，每一层检查一下是否对称。

        递归解法：
        
        其中左子树和右子树对称的条件：
        两个节点值相等，或者都为空
        左节点的左子树和右节点的右子树对称
        左节点的右子树和右节点的左子树对称
        
        """
        '''
        #1st iterative using list to store the node at each level and check the symmetry
        if root is None:
            return True
        q = deque()
        q.append(root)
        lsts = []
        while (len(q)):
            n = len(q)
            lst = []
            while(n > 0):
                item = q.popleft()
                if item is not None:
                    lst.append(item.val)
                    q.append(item.left)
                    q.append(item.right)
                    print ('item: ', item.val)
                else:
                    lst.append(None)
                n -= 1

            if lst[::-1] != lst[::]:
                print ('ddddd: ', lst)
                return False
        return True
        '''
        #2st recursive way;  not using list 
        if root is None:
            return True
        return self.isSymmRecursive(root.left, root.right)
        
    def isSymmRecursive(self, left, right):
        if left is None and right is None:
            return True
        elif left is None and right is not None:
            return False
        elif right is None and left is not None:
            return False
            
        if left.val != right.val:
            return False
        #if left.left == right.right and left.right == right.left:
        return self.isSymmRecursive(left.left, right.right) and self.isSymmRecursive(left.right, right.left)
        
                
                
        
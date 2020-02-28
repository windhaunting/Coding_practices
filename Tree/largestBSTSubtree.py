#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:22:45 2018

@author: fubao
"""



# 






#  Largest BST Subtree


'''
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:

    10
    / \
   5  15
  / \   \ 
 1   8   7
The Largest BST Subtree in this case is the highlighted one. 
The return value is the subtree's size, which is 3.

 

Hint:

You can recursively use algorithm similar to 98. Validate Binary Search Tree at each node of the tree, which will result in O(nlogn) time complexity.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?


'''


# 1ST 可以用之前那道Validate Binary Search Tree的方法来做，时间复杂度为O(nlogn) ?  O(n^2)，
这种方法是把每个节点都当做根节点，
来验证其是否是二叉搜索数，并记录节点的个数，若是二叉搜索树，就更新最终结果

 as it finds a largest BST - even though asymptotic complexity is not O(n). 
 Worst case performance is likely only when its there're no BST greater than size 1 (leaf)

、




1st recursive

 def dfs(root):
        if not root:
            return 0, 0, float('inf'), float('-inf')
        N1, n1, min1, max1 = dfs(root.left)
        N2, n2, min2, max2 = dfs(root.right)
        n = n1 + 1 + n2 if max1 < root.val < min2 else float('-inf')
        return max(N1, N2, n), n, min(min1, root.val), max(max2, root.val)
    return dfs(root)[0]
My dfs returns four values:

N is the size of the largest BST in the tree.
If the tree is a BST, then n is the number of nodes, otherwise it's -infinity.
If the tree is a BST, then min and max are the minimum/maximum value in the tree.





    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def isbst(root, minv, maxv):
            if root:
                return minv < root.val < maxv and isbst(root.left, minv, root.val) and isbst(root.right, root.val, maxv)
            return True
        
        def size(root):
            if root:
                return size(root.left) + size(root.right) + 1
            return 0
        
        if not root:
            return 0
    
        sentinel = TreeNode(None)
        q    = []
        ans  = 0
        q.append(root)
        q.append(sentinel)
        while q:
            node = q.pop(0)
            if node is sentinel:
                if ans > 1:
                    return ans
                if q:
                    q.append(sentinel)
                continue
                
            if isbst(node, -float('inf'), float('inf')):
                #print('isbst', node.val)
                ans = max(ans,size(node))
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans
    
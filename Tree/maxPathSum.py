#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 22:54:38 2018

@author: fubao
"""


# 124. Binary Tree Maximum Path Sum




'''

[LeetCode] Binary Tree Maximum Path Sum
Given a binary tree, find the maximum path sum.
The path may start and end at any node in the tree.
For example:
Given the below binary tree,
       1
      / \
     2   3
Return 6.

'''


# reference :  http://bangbingsyb.blogspot.com/2014/11/leetcode-binary-tree-maximum-path-sum.html


思路：
1. 与常规path sum不同，这题的path sum可以不起始于root，也可以不终止于leaf。

2. 这样的path可以归纳为两种情况：
(1) root->leaf path中的一段：即题目例子中的1-2或1-3。
(2) 两个节点之间经过它们lowest common ancestor (LCA)的path：即题目中的2-1-3。

3. 显然top-down的递归并不适用于这题，因为对于类型(2)的path，它的path sum同时取决于LCA左右sub path的最大值。而这样的path sum是无法通过top-down传递来获取的。

4. 所以这里可以采用bottom-up的递归方法:
对于节点x:
定义PS1(x)为从x出发向leaf方向的第一类path中最大的path sum。
定义PS2(x)为以x为LCA的第二类path中的最大path sum。
显然如果我们求得所有节点x的PS1 & PS2，其中的最大值必然就是要求的max path sum。

5. 如何求PS1(x)、PS2(x)?
(1) PS1(x) 、PS2(x)至少应该不小于x->val，因为x自己就可以作为一个单节点path。
(2) PS1(x) 、 PS2(x)可以从PS1(x->left)和PS1(x->right)来求得：
PS1(x) = max [ max(PS1(x->left), 0), max(PS1(x->right), 0) ] + x->val
PS2(x) = max(PS1(x->left), 0) + max(PS1(x->right), 0) + x->val
注意这里并不需要PS2(x->left) 以及 PS2(x->right) 因为子节点的2型path无法和父节点构成新的path。

6. 需要返回PS1(x)以供上层的节点计算其PS1 & PS2.

7. 对于leaf节点：PS1(x) = PS2(x) = x->val.


class Solution {
public:
    int maxPathSum(TreeNode *root) {
        int maxSum = INT_MIN;
        int ps1_root = findMaxPathSum(root, maxSum);
        return maxSum;
    }
    
    int findMaxPathSum(TreeNode *root, int &maxSum) {
        if(!root) return 0;
        
        int ps1_left = 0, ps1_right = 0;
        if(root->left) 
            ps1_left = max(findMaxPathSum(root->left,maxSum),0);
        if(root->right)
            ps1_right = max(findMaxPathSum(root->right,maxSum),0);
        
        int ps1_root = max(ps1_left, ps1_right) + root->val;    
        int ps2_root = ps1_left + ps1_right + root->val;
        maxSum = max(maxSum,max(ps1_root, ps2_root));
        
        return ps1_root;
    }
};




总结：

1. 解题的关键在于对path的分类以及应用top-down recursion。

2. 注意的细节是当x->left或x->right的第一类path sum为负数时，则这类path不应该传递到x：ln 13-16。

3. 代码并没有特殊处理leaf节点的情况。因为当root->left和root->right都不存在时，ps1_left和ps1_right均为初始值0：ln 12。于是ps1_root = ps2_root = root->val。



# python :

Updating node.val by the bigger one between left and right, and ignore them when none of them is positive.

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def path(node):
            if not node: return 0
            left, right = max(path(node.left), 0), max(path(node.right), 0)
            self.ans = max(self.ans, left + right + node.val)
            node.val += max(left, right)
            return node.val
            
        self.ans = float('-inf')
        path(root)
        return self.ans if root else 0
    
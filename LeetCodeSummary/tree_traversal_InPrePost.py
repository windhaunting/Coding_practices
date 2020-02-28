#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:21:02 2019

@author: fubao
"""

#
'''
preorder traversal
inorder traversal
postOrder traversal

'''


# recursive way:

# A function to do inorder tree traversal 
def printInorder(root): 
  
    if root: 
  
        # First recur on left child 
        printInorder(root.left) 
  
        # then print the data of node 
        print(root.val), 
  
        # now recur on right child 
        printInorder(root.right) 
        
    
# A function to do postorder tree traversal 
def printPostorder(root): 
  
    if root: 
  
        # First recur on left child 
        printPostorder(root.left) 
  
        # the recur on right child 
        printPostorder(root.right) 
  
        # now print the data of node 
        print(root.val), 
  
  
# A function to do preorder tree traversal 
def printPreorder(root): 
  
    if root: 
  
        # First print the data of node 
        print(root.val), 
  
        # Then recur on left child 
        printPreorder(root.left) 
  
        # Finally recur on right child 
        printPreorder(root.right)     
#
        
#iterative way:      
'''
a fancy way is to use a print or visit signal to record the when to print or visit

reference:
    https://www.youtube.com/watch?v=cIoGuSCU14A
    
e.g. 
   1
 2   3
4 5
    

use a stack

print 1
visit 2
visit 3

initialize the root as visit first
to put in the stack first
then pop the stack
if it is print, print:
else:put the left and right child into the stack as visiting
and put the root in the stack as print

'''

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        
        # 1st recursive
        #SUCCESS 2nd iterative way
        
        
        if root is None:
            return []
        stk = [(root, 0)]        # 1 is print or output, 0 is visiting
        
        lst_res = []
        while(len(stk)):
            
            # pop
            cur, flag = stk.pop(-1)
          
            if flag:
                lst_res.append(cur.val)
            else:
                if cur.right:
                    stk.append((cur.right, 0))
                    
                if cur.left:
                    stk.append((cur.left, 0))
                    
                stk.append((cur, 1))        # change to print
    
        return lst_res
    
    
    
        
def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        
        # 1st recursive        
        
        #SUCCESS 2nd iterative way
        
        if root is None:
            return []
        stk = [(root, 0)]        # 1 is print, 0 is visiting
        
        lst_res = []
        while(len(stk)):
            
            # pop
            cur, flag = stk.pop(-1)
            
            if flag:
                lst_res.append(cur.val)
            else:
                if cur.right:
                    stk.append((cur.right, 0))
                    
                stk.append((cur, 1))        # change to print
                
                if cur.left:
                    stk.append((cur.left, 0))
    
        return lst_res



def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        
        # 1st recursive        
        
        #SUCCESS 3rd iterative way
        
        if root is None:
            return []
        stk = [(root, 0)]        # 1 is print, 0 is visiting
        
        lst_res = []
        while(len(stk)):
            
            # pop
            cur, flag = stk.pop(-1)
            
            if flag:
                lst_res.append(cur.val)
            else:
                stk.append((cur, 1))        # change to print

                if cur.right:
                    stk.append((cur.right, 0))
                
                if cur.left:
                    stk.append((cur.left, 0))
    
        return lst_res
    
    

三种遍历
recursion
recursion的方法很简单 Time O(n) Space O(1)

class Solution(object):
    def orderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
         
        self.traverse(root, res)
        return res
    def traverse(self, root, res):
        if not root:
            return;
        res.append(root.val) # preorder
        self.traverse(root.left, res)
        ## res.append(root.val) # inorder
        self.traverse(root.right, res)
        ## res.append(root.val) # postorder
        
        
iterative
因为不能使用recursion，所以我们要模拟构建栈。

前序遍历(pre-order):
根->左->右1. 对root异常处理 2.cur 指向root, 循环条件为node!=null || !stack.isEmpty() 3.当cur不为空，就压入stack,并将元素加入结果，cur继续往左边找 4.当cur为空，就cur就为pop出的栈顶元素,.cur继续往右边找. 5.返回最终结果集合.
T O(n)
S O(h)

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        res = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                res.append(node.val)
                node = node.left
            node = stack.pop()
            node = node.right
            
        return res
中序遍历
本质上是一样的，先访问左孩子所以就一路到底

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        res = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
            
        return res
后序遍历
这个需要一点技巧以及练习，因为根节点需要访问两次，所以就需要判断是否已经访问过右节点了

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            peak = stack[-1]
            if peak.right and peak.right != pre: # 如果当前栈顶元素的右结点存在并且还没访问过（也就是右结点不等于上一个访问结点）就访问右结点 
                root = peak.right
            else: # 如果栈顶元素右结点是空或者已经访问过，那么说明栈顶元素的左右子树都访问完毕 需要把栈顶元素加入结果并且回溯上一层

                stack.pop()
                res.append(peak.val)
                pre = peak
        return res
不过还有一种更加巧妙的办法，前序遍历和后续遍历能否直接颠倒呢？答案是否定的，我们来看看前序遍历：根-左子树-右子树
后序遍历：左子树-右子树-根 把前序遍历倒过来：右子树-左子树-根 ！左右子树相反，不能直接倒！
但是这题，哼哼哼，先左子树入栈，在右子树入栈！最后输出颠倒一下即可！

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if not root: return []
        ans,q=[],[]
        q.append(root)
        while q:
            cur=q.pop()          
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)
            ans.append(cur.val)
        return ans[::-1]
    
    
    
# for inorder traverse, we can use Morris traversal without using stack or recursion.
# the space complexity is O(1)
        
#  https://www.educative.io/edpresso/what-is-morris-traversal
Morris Inorder Traversal    
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left_node = None
		self.right_node = None

def Morris(root): 
	# Set current to root of binary tree 
	curr = root 
	
	while(curr is not None): 
		
		if curr.left_node is None: 
			print curr.data, 
			curr = curr.right_node 
		else: 
			# Find the previous (prev) of curr 
			prev = curr.left_node 
			while(prev.right_node is not None and prev.right_node != curr): 
				prev = prev.right_node 

			# Make curr as right child of its prev 
			if(prev.right_node is None): 
				prev.right_node = curr 
				curr = curr.left_node 
				
			# fix the right child of prev
			else: 
				prev.right_node = None
				print curr.data
				curr = curr.right_node 
			

root = Node(4) 
root.left_node = Node(2) 
root.right_node = Node(5) 
root.left_node.left_node = Node(1) 
root.left_node.right_node = Node(3) 

Morris(root) 

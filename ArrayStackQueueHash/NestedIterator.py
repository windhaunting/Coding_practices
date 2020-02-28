#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 10:19:55 2018

@author: fubao
"""


'''

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):


    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList
        self.stk = []           # stack store the NestedInteger type class
        
        # put in the stack backward, 
        for i in range(0, len(nestedList)):
            self.stk.append(nestedList[i])

    def next(self):
        """
        :rtype: int
        """
        ele = self.stk.pop(0)
        return ele.getInteger()
     
    
    def hasNext(self):
        """
        :rtype: bool
        """
        # pop and then check if it's integer or list, if it's list, pop 
        # and then put in the stack again, call hasNext, if it's an integer, return True
        if len(self.stk):
            
            ele = self.stk[0]
            if ele.isInteger():
                return True #  ele.getInteger()
            else:
                #pop 
                tmpNestInt = self.stk.pop(0)
                tmpNestlst = tmpNestInt.getList()
                for i in range(len(tmpNestlst)-1,-1,-1):
                    self.stk.insert(0, tmpNestlst[i])

                return self.hasNext()
                       
        return False
        
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())



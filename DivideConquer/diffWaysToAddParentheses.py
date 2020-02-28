#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 12:11:44 2018

@author: fubao
"""



# 241. Different Ways to Add Parentheses


'''
parenthesis

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

'''


'''
e.g.
 ways("2-1-1")
 
 case 1: ways("2")  X ways("1-1") = 2-0 = 2         # X means cartesian product
 case 2 ways("2-1") X ways("1")  = 1-1 = 0
 {2, 0}
 
e.g.
 ways ("2*3-4*5")
 
 => ways("2") X ways("3-4*5")
U=> ways("2*3") X ways("4*5")
U=> ways("2*3-4") X ways("5")

'''

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        
        '''
        #1st approach recursive way
        
        def calcMath(num1, num2, operator):           #python does not have switch/case
            res = 0
            if operator == "+":
                res = num1 + num2
            elif operator == "-":
                res = num1 - num2
            elif operator == "*":
                res = num1 * num2
            return res
            
        result = []
        for i, c in enumerate(input):
            if  c == "+" or c == "-" or c == "*":
                leftSubStr  = input[0:i]
                rightSubStr = input[i+1::]
                
                leftLst = self.diffWaysToCompute(leftSubStr)
                rightLst = self.diffWaysToCompute(rightSubStr)
                #print ("ttttt  ", i, c, leftLst, rightLst)
                for ls in leftLst:
                    for rs in rightLst:
                        rs = calcMath(ls, rs, c)
                        result.append(rs)
                #print ("ttttt  ", result)
        if len(result) == 0:
            result.append(int(input))
        return result
        '''
        
        #2nd  optimization 1st method
        #in the previous calculations, there are repeated calculation of substring with same left substring and right substring calculation
        
        def calcMath(num1, num2, operator):           #python does not have switch/case
            res = 0
            if operator == "+":
                res = num1 + num2
            elif operator == "-":
                res = num1 - num2
            elif operator == "*":
                res = num1 * num2
            return res
            
       
            
        def  diffWaysToComputeHelper(input, start, end):
            
            result = []
            strKey = str(start) + "-" + str(end)
            if strKey in dic:
                result = dic[strKey]
                return result
            #print ("sssss  ", result, start, end)
            for i, c in enumerate(input[start:end+1]):
                if  c == "+" or c == "-" or c == "*":           #or if c in "+-*"
                    leftLst = diffWaysToComputeHelper(input, start, start+i-1 )
                    rightLst = diffWaysToComputeHelper(input, start+i+1, end)
                    #print ("xxxxx  ", i, c, leftLst, rightLst, start, end)
                    for ls in leftLst:
                        for rs in rightLst:
                            rs = calcMath(ls, rs, c)
                            result.append(rs)
                           
            #print ("ttttt  ", result, start, end, input[start:end+1])
            if len(result) == 0:
                result.append(int(input[start:end+1]))
            dic[strKey] = result
            return result
        
        dic = {}                #memoization
        return diffWaysToComputeHelper(input, 0, len(input)-1)



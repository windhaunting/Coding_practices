#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:20:34 2018

@author: fubao
"""


'''

1. Given a 2D array of size width*height how many ways are there to
 go from (0, 0) to (width-1, 0) given the available
 moves from (x,y) are (x+1, y+{1,0,-1}).

'''


'''
e.g.

* x x
x x x
x x x
o x x

=> 
   * 
   x x
   x x x
   o 

* x x
o x x

* 
x x 
o x x

'''

# 1st naive way to use traverse until arrive the last row or last line to stop for each path with BFS

def pathNumFind(grid):
    '''
    start from 0,0 to (width-1) as above use graph traversal using BFS 
    '''
    
    #use bfs
    if not grid or len(grid) == 0:
        return 0
    
    m = len(grid)         # width;  vertical
    n = len(grid[0])      # length
    stInd = (0, 0)
    
    que = []        # queue
    
    que.append((stInd, 1))
    resPathNum = 0
    visited = set()
    visited.add(stInd)
    while (len(que)):
        #pop 
        cur = que.pop()
        x = cur[0][0]
        y = cur[0][1]
        lastPathNum = cur[1]
                        
        inc = [-1, 0, 1]
        for i in inc:
            if (x+1) < 0 or (x+1) > n or (y+i) < 0 or (y+i) > m:
                continue
            
            newX = (x+1, y+i)  #new next node
            if newX not in visited:   #no update for lastPathNum
                newPathNum = lastPathNum
            else:
                newPathNum = lastPathNum + 1  #every node's path number could be got, but acutally no need to store here.
            
            if newX == (m-1, 0):
                resPathNum += 1
                
            que.append((newX, newPathNum))
            
    return resPathNum

        
            
m = 3
n = 3
grid = [[0] * n for i in range(m)]
   
print ("pahtNum: ",pathNumFind(grid))
        

#2nd use Dynamic programming: 

#  node x can get (x-1, y-1), (x-1, y), (x-1, y+1)
# p[i][j] for number of paths node from (0, 0) to (i, j)
# p[i][j] = p[i-1][j-1] + p[i-1][j] + p[i-1][j+1]
def pathNumFind2(m, n):
    p = [[0 for i in range(n)] for j in range(m)]
    p[0][0] = 1
    
    #for k in range(m):
    #    p[k][0] = 1

    print ('p', p)
    for i in range(1, m):
        for j in range(0,n):
            if j-1 >= 0:
                p[i][j] = p[i-1][j-1]
            if j+1 < n:
                p[i][j] += p[i-1][j+1]
            p[i][j] += p[i-1][j]
            
            print ("p i j : ", i, j, p[i][j])
    return p[m-1][0]
    

'''
* x x
x x x
o x x

'''
print ("pahtNum23: ",pathNumFind2(2, 3))

print ("pahtNum33: ",pathNumFind2(3, 3))
        


# 3rd reduce space using 
 #2nd how to reduce the space to one dimension?   three column ?
        # DP p[j] = p[j] +p[j-1] + p[j+1]
        '''
        
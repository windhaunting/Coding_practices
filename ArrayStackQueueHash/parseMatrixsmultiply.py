#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 08:28:03 2018

@author: fubao
"""




# Leetcode 311  Sparse matrix multiplication  dot product



'''

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
                  
'''


# if it's sparse vector A and B , m non-zero in A,  n nonzero in B;

complexity o(m*n); o(m*logn) if B sorted by index, 
 o(m+n) if A and B are all sorted
O(min(m,n)) if we use hashmap to store each index and its non-zero value in A or B




# reference:  http://blog.csdn.net/jmspan/article/details/51205354


方法一：普通矩阵乘法


public class Solution {  
    public int[][] multiply(int[][] A, int[][] B) {  
        int[][] C = new int[A.length][B[0].length];  
        for(int i=0; i<A.length; i++) {  
            for(int j=0; j<A[i].length; j++) {  
                if (A[i][j] == 0) continue;  
                for(int k=0; k<B[0].length; k++) {  
                    if (B[j][k] == 0) continue;  
                    C[i][k] += A[i][j] * B[j][k];  
                }  
            }  
        }  
        return C;  
    }  
}  


方法二：使用哈希映射来存放非0数字。
public class Solution {  
    private Map<Integer, Map<Integer, Integer>> map(int[][] m) {  
            
        Map<Integer, Map<Integer, Integer>> rows = new HashMap<>();  
        for(int i=0; i<m.length; i++) {  
            for(int j=0; j<m[i].length; j++) {  
                if (m[i][j]==0) continue;  
                Map<Integer, Integer> cols = rows.get(i);  
                if (cols == null) {  
                    cols = new HashMap<>();  
                    rows.put(i, cols);  
                }  
                cols.put(j, m[i][j]);  
            }  
        }  
        return rows;  
    }  
    public int[][] multiply(int[][] A, int[][] B) {  
        int[][] C = new int[A.length][B[0].length];  
        Map<Integer, Map<Integer, Integer>> arows = map(A);  
        Map<Integer, Map<Integer, Integer>> brows = map(B);  
        for(int i: arows.keySet()) {  
            Map<Integer, Integer> acol = arows.get(i);  
            for(int j: acol.keySet()) {  
                Map<Integer, Integer> bcol = brows.get(j);  
                if (bcol == null) continue;  
                int a = acol.get(j);  
                for(int l: bcol.keySet()) {  
                    C[i][l] += a * bcol.get(l);  
                }  
            }  
        }  
        return C;  
    }  
}  
                
                
方法三：使用链表存储稀疏矩阵。

public class Solution {  
    public int[][] multiply(int[][] A, int[][] B) {  
        List<Line> arows = new ArrayList<>();  
        Line line = new Line();  
        for(int i=0; i<A.length; i++) {  
            for(int j=0; j<A[i].length; j++) {  
                if (A[i][j] != 0) {  
                    line.p1 = i;  
                    line.p2.add(j);  
                }  
            }  
            if (line.p1 != -1) {  
                arows.add(line);  
                line = new Line();  
            }  
        }  
        List<Line> bcols = new ArrayList<>();  
        line = new Line();  
        for(int j=0; j<B[0].length; j++) {  
            for(int i=0; i<B.length; i++) {  
                if (B[i][j] != 0) {  
                    line.p1 = j;  
                    line.p2.add(i);  
                }  
            }  
            if (line.p1 != -1) {  
                bcols.add(line);  
                line = new Line();  
            }  
        }  
          
        int[][] C = new int[A.length][B[0].length];  
          
        for(int i=0; i<arows.size(); i++) {  
            for(int j=0; j<bcols.size(); j++) {  
                Line arow = arows.get(i);  
                Line bcol = bcols.get(j);  
                int a=0, b=0;  
                while (a<arow.p2.size() && b<bcol.p2.size()) {  
                    if (arow.p2.get(a) == bcol.p2.get(b)) {  
                        // System.out.printf("arow.p1=%d, bcol.p1=%d, arow.p2.get(%d)=%d, bcol.p2.get(%d)=%d\n",   
                        // arow.p1, bcol.p1, a, arow.p2.get(a), b, bcol.p2.get(b));  
                        C[arow.p1][bcol.p1] += A[arow.p1][arow.p2.get(a)] * B[bcol.p2.get(b)][bcol.p1];  
                        a ++;  
                        b ++;  
                    } else if (arow.p2.get(a) > bcol.p2.get(b)) b ++;  
                    else a ++;  
                }  
            }  
        }  
          
        return C;  
    }  
}  
  
class Line {  
    int p1 = -1;  
    List<Integer> p2 = new ArrayList<>();  
}  


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:10:41 2018

@author: fubao
"""



#  304. Range Sum Query 2D - Immutable


'''
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.

'''


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
        
        
Approach #3 (Caching Rows) [Accepted] To find the region sum, we just accumulate the sum in the region row by row.


Intuition

Remember from the 1D version where we used a cumulative sum array? Could we apply that directly to solve this 2D version?

Algorithm

Try to see the 2D matrix as mm rows of 1D arrays. To find the region sum, we just accumulate the sum in the region row by row.

private int[][] dp;

public NumMatrix(int[][] matrix) {
    if (matrix.length == 0 || matrix[0].length == 0) return;
    dp = new int[matrix.length][matrix[0].length + 1];
    for (int r = 0; r < matrix.length; r++) {
        for (int c = 0; c < matrix[0].length; c++) {
            dp[r][c + 1] = dp[r][c] + matrix[r][c];
        }
    }
}

public int sumRegion(int row1, int col1, int row2, int col2) {
    int sum = 0;
    for (int row = row1; row <= row2; row++) {
        sum += dp[row][col2 + 1] - dp[row][col1];
    }
    return sum;
}
Complexity analysis

Time complexity : O(m)O(m) time per query, O(mn)O(mn) time pre-computation. The pre-computation in the constructor takes O(mn)O(mn) time. The sumRegion query takes O(m)O(m) time.

Space complexity : O(mn)O(mn). The algorithm uses O(mn)O(mn) space to store the cumulative sum of all rows.




# Approach #4 (Caching Smarter) [Accepted] accumulated region to origin (0, 0)

Algorithm

We used a cumulative sum array in the 1D version. We notice that the cumulative sum is computed with respect to the origin at index 0. Extending this analogy to the 2D case, we could pre-compute a cumulative region sum with respect to the origin at (0, 0)(0,0).

Sum OD
Sum(OD) is the cumulative region sum with respect to the origin at (0, 0).

How do we derive Sum(ABCD)Sum(ABCD) using the pre-computed cumulative region sum?

Sum OB
Sum(OB) is the cumulative region sum on top of the rectangle.

Sum OC
Sum(OC) is the cumulative region sum to the left of the rectangle.

Sum OA
Sum(OA) is the cumulative region sum to the top left corner of the rectangle.

Note that the region Sum(OA)Sum(OA) is covered twice by both Sum(OB)Sum(OB) and Sum(OC)Sum(OC). We could use the principle of inclusion-exclusion to calculate Sum(ABCD)Sum(ABCD) as following:

Sum(ABCD) = Sum(OD) - Sum(OB) - Sum(OC) + Sum(OA) Sum(ABCD)=Sum(OD)−Sum(OB)−Sum(OC)+Sum(OA)

private int[][] dp;

public NumMatrix(int[][] matrix) {
    if (matrix.length == 0 || matrix[0].length == 0) return;
    dp = new int[matrix.length + 1][matrix[0].length + 1];
    for (int r = 0; r < matrix.length; r++) {
        for (int c = 0; c < matrix[0].length; c++) {
            dp[r + 1][c + 1] = dp[r + 1][c] + dp[r][c + 1] + matrix[r][c] - dp[r][c];
        }
    }
}

public int sumRegion(int row1, int col1, int row2, int col2) {
    return dp[row2 + 1][col2 + 1] - dp[row1][col2 + 1] - dp[row2 + 1][col1] + dp[row1][col1];
}
Complexity analysis

Time complexity : O(1)O(1) time per query, O(mn)O(mn) time pre-computation. The pre-computation in the constructor takes O(mn)O(mn) time. Each sumRegion query takes O(1)O(1) time.

Space complexity : O(mn)O(mn). The algorithm uses O(mn)O(mn) space to store the cumulative region sum.


'''


#   Range Sum Query 2D - Mutable 二维区域和检索 - 可变

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.



# binary index tree

#
class NumMatrix(object):

def __init__(self, matrix):
    if not matrix:
        return
    self.m, self.n = len(matrix), len(matrix[0])
    self.matrix, self.bit = [[0]*(self.n) for _ in range(self.m)], [[0]*(self.n+1) for _ in range(self.m+1)]
    for i in range(self.m):
        for j in range(self.n):
            self.update(i, j, matrix[i][j])

def update(self, row, col, val):
    diff, self.matrix[row][col], i = val-self.matrix[row][col], val, row+1
    while i <= self.m:
        j = col+1
        while j <= self.n:
            self.bit[i][j] += diff
            j += (j & -j)
        i += (i & -i)
    
def sumRegion(self, row1, col1, row2, col2):
    return self.sumCorner(row2, col2) + self.sumCorner(row1-1, col1-1) - self.sumCorner(row1-1, col2) - self.sumCorner(row2, col1-1)
    
def sumCorner(self, row, col):
    res, i = 0, row+1
    while i:
        j = col+1
        while j:
            res += self.bit[i][j]
            j -= (j & -j)
        i -= (i & -i)
    return res

// time should be O(log(m) * log(n))
Explanation of Binary Indexed Tree :
https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/


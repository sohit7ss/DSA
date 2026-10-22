from typing import List


# M-1 _brute
class Solution:
    def markinfinity(self,matrix, row, col):
        r = len(matrix)
        c = len(matrix[0])

        for i in range(0,r):
            if matrix[i][col] != 0:                     # O(m)
                matrix[i][col] = float("inf")
        
        for j in range(0,c):                            #O(n)
            if matrix[row][j] != 0:
                matrix[row][j] = float("inf")
                
                                                        # O(m + n)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix) 
        c = len(matrix[0])

        for i in range(0,r):
            for j in range(0,c):                    #  O(m * n)
                if matrix[i][j] == 0:
                    self.markinfinity(matrix, i, j)     #  O((m + n)(n * m))
        
        for i in range(0,r):
            for j in range(0,c):                        #  O(m * n)
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0




# TC = O((m + n)(n * m)) + O(m * n)


# M-2 _better
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        # Find all rows and columns containing 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Set rows to zero
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0

        # Set columns to zero
        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0





class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])

        row_trace = [0 for _ in range(r)]
        cols_trace = [0 for _ in range(c)] 

        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j] == 0:
                    row_trace[i] = -1
                    cols_trace[j] = -1
        
        for i in range(0,r):
            for j in range(0,c):
                if row_trace[i] == -1 or cols_trace[j] == -1:
                    matrix[i][j] = 0
        
        return matrix
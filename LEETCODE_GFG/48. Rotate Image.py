matrix = [[1,2,3],[4,5,6],[7,8,9]]

n = len(matrix)

result = [[0]* n for _ in range(n)]


for i in range(n):
    for j in range(n):
        result[j][(n-1)-i] = matrix[i][j]



print(result)


from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
    
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(0,n):
            matrix[i].reverse()
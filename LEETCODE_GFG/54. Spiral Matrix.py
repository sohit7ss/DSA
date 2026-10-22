from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        r = len(matrix)
        c = len(matrix[0])

        left = 0
        top = 0
        right = c
        bottom = r

        while left < right and top < bottom:

            # Top row
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            # Right column
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            # Bottom row
            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom - 1][i])
                bottom -= 1

            # Left column
            if left < right:
                for i in range(bottom - 1, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
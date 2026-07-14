class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        n = len(matrix[0])
        R = len(matrix[0]) * len(matrix) - 1
        while L<= R:
            M = (L + R) // 2
            col = M % n
            row = M // n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                L = M+1
            else:
                R = M-1
        return False
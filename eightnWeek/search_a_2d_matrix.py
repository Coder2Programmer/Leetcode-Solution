class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        row_size, col_size = len(matrix[0]), len(matrix)
        low, high = 0, row_size * col_size
        while low < high:
            mid = low + (high - low) // 2
            if matrix[mid//row_size][mid%row_size] < target:
                low = mid + 1
            else:
                high = mid
        return (low < row_size * col_size 
                and matrix[low//row_size][low%row_size] == target)

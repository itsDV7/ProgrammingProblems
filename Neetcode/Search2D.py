class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            mid = top + (bottom - top)//2
            if matrix[mid][0] > target:
                bottom = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
        if not top <= bottom:
            return False
        left = 0
        right = len(matrix[mid]) - 1
        while left <= right:
            m = left + (right - left)//2
            if matrix[mid][m] == target:
                return True
            if matrix[mid][m] < target:
                left = m + 1
            else:
                right = m - 1
        return False

# Another / Better Approach -> Flatten the matrix, then directly work with matrix elements.
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         rows = len(matrix)
#         cols = len(matrix[0])

#         low = 0
#         high = (rows * cols) - 1

#         while low <= high:
#             mid = (low + high) // 2

#             i = mid // cols
#             j = mid % cols

#             if matrix[i][j] == target:
#                 return True
#             elif matrix[i][j] < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return False

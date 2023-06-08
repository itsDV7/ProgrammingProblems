class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = 0
        m = len(grid[0]) - 1

        count = 0
        while m >= 0 and n < len(grid):
            if grid[n][m] < 0:
                count += len(grid) - n
                m -= 1
            else:
                n += 1

        return count

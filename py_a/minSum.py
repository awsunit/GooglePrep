# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # handle top row to make logic in for-loops cleaner
        for col in range(1, n):
            grid[0][col] += grid[0][col-1]

        for row in range(1, m):
            for col in range(n):
                if col == 0:
                    # the only option is the one above us
                    grid[row][col] += grid[row-1][col]
                else:
                    smallest_path = min(grid[row-1][col], grid[row][col-1])
                    grid[row][col] += smallest_path




        return grid[m-1][n-1]

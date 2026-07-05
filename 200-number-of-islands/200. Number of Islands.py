from collections import deque 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            # Base Case 1
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            # Base Case 2
            if grid[r][c] == "0":
                return

            # Base Case 3
            if (r, c) in visited:
                return
            visited.add((r,c))
            dfs(r - 1, c)   # Up
            dfs(r + 1, c)   # Down
            dfs(r, c - 1)   # Left
            dfs(r, c + 1)   # Right
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        islands = 0

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    dfs(i, j)

        return islands
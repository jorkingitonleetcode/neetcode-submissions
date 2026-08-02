class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # go through each thing that has a 1
        # run DFS, if it is a 1, it is valid
        # if it is a 0, it is not valid point to go
        # as we're going through this, set the 0s to 1s

        def dfs(i, j):

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return 0

            if grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i + 1, j)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i, j - 1)
                return 1

        island_count = 0
        for x in range(0, len(grid)):
            for y in range(0, len(grid[0])):
                if dfs(x,y) == 1:
                    island_count += 1
        
        return island_count
                    

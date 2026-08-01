class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]
        # in this case the issue is that xy would represent the amount of
        # paths to the destination
        # since we are going straight left  or right, this will naturally go 
        # to the right corner
        # say if we started from some random spot, same idea
        # the property that 
        def dfs(x,y):
            if x >= m  or  y >= n:
                return 0
            if x == m-1 and y == n-1:
                return 1
            if memo[x][y] != -1:
                return memo[x][y]
            memo[x][y] = dfs(x, y+1) + dfs(x+1, y)
            return memo[x][y]
        
        return dfs(0,0)
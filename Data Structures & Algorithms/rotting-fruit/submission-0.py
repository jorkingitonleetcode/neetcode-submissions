class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        # first find the rotting orange 
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j)) 
                if grid[i][j] == 1:
                    fresh += 1
        
        # start bfs from rotten bananas
        # when everyting is -1 then  
        
        min_minutes = 0
        
        while(q and fresh > 0):
            
            # pop all of the ones in queue and add it 
            curr_len = len(q)
            for _ in range(0, curr_len):
                (x,y) = q.popleft()
                

                if y-1 >= 0 and grid[x][y-1] == 1:
                    q.append((x, y-1))
                    fresh -= 1
                    grid[x][y-1] = 2
                if x-1 >= 0 and grid[x-1][y] == 1:
                    q.append((x-1,y))
                    fresh -= 1
                    grid[x-1][y] = 2
                if y + 1 < len(grid[0]) and grid[x][y+1] == 1:
                    q.append((x,y+1))
                    fresh -= 1
                    grid[x][y+1] = 2
                if x  + 1 < len(grid) and grid[x +1][y] == 1:
                    q.append((x+1,y))
                    fresh -= 1
                    grid[x+1][y] = 2
            min_minutes += 1
    
        return min_minutes if fresh == 0 else -1
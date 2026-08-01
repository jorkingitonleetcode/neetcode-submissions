class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # dp[i][j] i,j represents the number of coins 
        # at i for the coin
        # at j for the amount
        # setup dp
        
        dp = {}
        

        def dfs(i, total):
            if total < 0:
                return 0
            elif i >= len(coins):
                return 0
            elif total == 0:
                return 1
            
            if (i, total) in dp:
                return dp[(i,total)]
    
            # want to do 2 things 
            # add the current coin OR
            # skip the coin, and go next
            dp[(i, total)] = dfs(i+1, total ) + dfs(i, total - coins[i])

            return dp[(i, total)]
        
        return dfs(0, amount)
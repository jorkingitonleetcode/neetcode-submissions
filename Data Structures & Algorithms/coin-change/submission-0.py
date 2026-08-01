class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # What we can do is a bottom up approach by constructing it without skipping
        # let dp[j] be the total coins
        # let j represent the amount
        # now the trick is this, we capture the last coin in the amounts
        # initializing dp
        if amount == 0:
            return 0
        coins.sort()
        inf = 999999999
        dp = [inf] * (amount + 1)
        dp[0] = 0


        for i in range(0, amount + 1):
            
            for j in range(0,len(coins)):
                # the last minimum num coins
                leftover = i - coins[j]
                if leftover >= 0 and dp[leftover] != -1:
                    dp[i] = min(dp[i], 1 + dp[leftover])
                

        if dp[amount] >= inf:
            return -1
        return dp[amount]

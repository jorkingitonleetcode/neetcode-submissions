class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # min cost climbing stairs
        # what to define dp[i]?
        # well here dp[i] is the cost at some staircase?

        # let us define i as the step, and dp[i] the min cost at this step.
        dp = [0] * len(cost)

        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[-2], dp[-1])

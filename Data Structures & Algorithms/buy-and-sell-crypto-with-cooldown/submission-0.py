class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Idea : DFS!
        # why is it a 2D Dynamic pointer here though?

        # it is 2 dimensional, but the second dim is just a true or false
        # i was right to think that it is 
        # the necessity

        # let the keys be i and buying: true or false,
        # question what is the max profit if we CAN sell on day i, 
        # what is the max profit if we CAN buy on day i 

        memo = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i,buying)]

            if buying == True:
                memo[(i,buying)] = max(dfs(i + 1, not buying ) - prices[i], dfs(i+1, buying) )
                return memo[(i, buying)]
            else:   
                memo[(i, False)] = max(dfs(i + 2, True) + prices[i] , dfs(i + 1, False))
                return memo[(i, False)]
        return dfs(0, True)

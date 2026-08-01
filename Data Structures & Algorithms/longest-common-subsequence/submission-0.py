class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # this is a dynamic problem
        # What can i do here?
        # dp[i][j], where i can track the letters of the first word 
        # and j can track the letters of the second.
        # dp[i][j] would represent the longest subseqence of 
        # both strings at that point
        # Now the question is how do i do this 
        
        # dp[i][j] is actually the lognest sub sequence beased off of strigns 
        dp = [[-1]* len(text2) for _ in range(len(text1))] 
        # note for memoization, we do not need to create something from
        # past states, rather, we create things from the exploration.
        # what this fucntion is saying is, let's start from 0,0 and see how many
        # strings are connected.

        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            elif dp[i][j] != -1:
                return dp[i][j]
            
            if text1[i] == text2[j]:
                # iterate together ifthey are the same
                # this just means that we are in agreement that we can
                # start a new string here.
                dp[i][j] = 1 + dfs(i+1, j+1)
            else: 
                # explore the possibilites from both directions
                dp[i][j] = max(dfs(i+1 , j), dfs(i, j+1))

            return dp[i][j]
        return dfs(0,0)
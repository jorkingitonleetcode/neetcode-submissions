class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # what is dp?
        # okay so dp[i] would be true or false at string len s 

        dp = [False] * (len(s) + 1)

        # Idea:
        # Go through each index in the string
        # If dp[i-len[word]] == true or s[:i] is a word in the word dict
        # dp[current_index] == true
        # If it isnt see if we can make a combination of 
        # the string based off of past results.
    
        # yeay
        # if 
        # Go through each word based on the substring.
        
        dp[0] = True
        for i in range(0, len(s)+1):
            # at each iteration, we need to contstruct
            for word in wordDict:
                for k in range(0, i+1):
                    if s[k:i] == word and dp[k] == True:
                        dp[i] = True
                                
        return dp[len(s)]
                    
        
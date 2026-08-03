class Solution:
    def isValid(self, s: str) -> bool:
        # last known
        closing = []
        openings = {'[' : ']', '{': '}', '(':')'}
        if s[0] not in openings:
            return False
        for c in s:
            # start with left 
            if c in openings:
                closing.append(openings[c])
            elif len(closing) > 0:
                if closing[-1] == c:
                    closing.pop()
        
        if len(closing) == 0:
            return True
        else:
            return False
           
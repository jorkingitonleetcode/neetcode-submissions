class Solution:
    def isValid(self, s: str) -> bool:
        # last known
        closing = []
        opening = []
        mapping = {'[' : ']', '{': '}', '(':')'}
        
        for c in s:
            # start with left 
            if c in mapping:
                closing.append(mapping[c])
                opening.append(c)
            elif len(closing) > 0 and len(opening) > 0:
                if closing[-1] == c:
                    closing.pop()
                    opening = opening[1:]
                else:
                    return False
            else:
                return False
        
        if len(closing) == 0:
            return True
        else:
            return False
           
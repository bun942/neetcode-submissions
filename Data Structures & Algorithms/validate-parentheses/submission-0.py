class Solution:
    def isValid(self, s: str) -> bool:
        sp = []
        arr = {')' : '(','}' : '{',']' : '['}
        for x in s:
            if x not in arr:
                sp.append(x)
            elif x in arr:
                if not sp:
                    return False
                elif arr[x] == sp[-1]:
                    sp.pop()
                else:
                    return False
        
        if len(sp) == 0:
            return True 
        else:
            return False
                
        
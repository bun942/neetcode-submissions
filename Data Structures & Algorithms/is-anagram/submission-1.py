class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        val_1={}
        val_2={}
        if len(s) == len(t):
            for x in range(len(s)):
                val_1[s[x]] = val_1.get(s[x],0)+1
                val_2[t[x]] = val_2.get(t[x],0)+1
            if val_1 == val_2:
                return True
            else:
                return False
        else:
            return False
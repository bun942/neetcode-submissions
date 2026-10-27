class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split())
        n_s = ""
        for i in s:
            if i.isalnum():
                n_s +=i
        s = n_s.lower()
        # print(s)

        l,r = 0,len(s)-1
        # print(r)
        while l < r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return False
        
        return True 
        
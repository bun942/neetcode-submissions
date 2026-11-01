class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0
        max_len = 0
        if not s:
            return max_len
        my_set = set() 
        while r < len(s):
            if s[r] not in my_set:
                my_set.add(s[r])
                r+=1
            else:
                my_set.discard(s[l])
                l+= 1
            max_len = max(max_len, len(my_set))
            
        
        return max_len
        
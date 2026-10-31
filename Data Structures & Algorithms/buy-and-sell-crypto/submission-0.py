class Solution:
    def maxProfit(self, p: List[int]) -> int:
        l = 0 
        r = 1
        pf = 0 

        while r < len(p):
            current = p[r] - p[l]
            if current > pf:
                pf = current
            elif p[r] < p[l]:
                l = r
            
            r +=1
        return pf    
        
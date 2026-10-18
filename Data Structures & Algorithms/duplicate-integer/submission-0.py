class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map_c={}
        for x in nums:
            if x in map_c:
                return True
            else:
                map_c[x] = 1
        
        return False 
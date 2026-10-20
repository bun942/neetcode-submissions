class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i , val in enumerate(nums):
            com = target - val 

            if com in m:
                return [m[com],i]
                break 
            
            m[val] = i 
        
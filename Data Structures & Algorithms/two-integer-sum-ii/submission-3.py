class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        l = 0
        r = len(n)-1

        c = False

        while c != True:
            if t == n[l] + n[r]:
                return [(l+1),(r+1)]
            elif t < (n[l]+n[r]):
                r-=1
            elif t > (n[l]+n[r]):
                l+=1
            else:
                l+=1
                r-=1

        
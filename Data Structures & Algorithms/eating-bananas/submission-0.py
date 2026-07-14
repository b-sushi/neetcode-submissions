class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L  = 1
        R = max(piles)
        ans = 0 
        while L <= R:
            M = (L+R)//2
            tot = 0
            for i in range(len(piles)):
                tot += math.ceil(piles[i] / M)
            if tot > h:
                L = M+1
            else:
                ans = M
                R = M-1
        return ans
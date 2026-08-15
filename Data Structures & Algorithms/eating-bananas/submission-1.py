import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        while L <= R:
            M =  (L + R) // 2
            time = 0
            for num in piles:
                time += math.ceil(num / M)
            if time <= h:
                ans = M
                R = M - 1
            else:
                L = M + 1
        return ans
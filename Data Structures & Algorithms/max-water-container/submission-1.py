class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_vol = 0
        vol = 0
        while l < r:
            vol = (r - l) * min(heights[l], heights[r])
            max_vol = max(vol, max_vol)
            if l < r and heights[l] > heights[r]:
                r -= 1
            elif l < r and heights[l] <= heights[r]:
                l +=1
        return max_vol 


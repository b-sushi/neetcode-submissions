class Solution:
    def trap(self, height: List[int]) -> int:
         l = 0
         r = len(height) - 1
         left_max = height[l]
         right_max = height[r]
         result = 0
         while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(height[l], left_max)
                result += max(left_max - height[l],0)
            else:
                r -=1
                right_max = max(height[r], right_max)
                result += max(right_max - height[r],0)
         return result 
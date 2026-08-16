class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = global_max = nums[0]
        
        for num in nums[1:]:
            # Precompute products before updating cur_max
            p1, p2 = cur_max * num, cur_min * num
            cur_max = max(num, p1, p2)
            cur_min = min(num, p1, p2)
            global_max = max(global_max, cur_max)
            
        return global_max
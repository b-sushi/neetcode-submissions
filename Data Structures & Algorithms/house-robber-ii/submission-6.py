class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def rob_range(start: int, end: int) -> int:
            memo = {}
            def steal(i: int) -> int:
                if i < start:
                    return 0
                if i == start:
                    return nums[start]
                if i in memo:
                    return memo[i]
                memo[i] = max(steal(i - 1), steal(i - 2) + nums[i])
                return memo[i]
                
            return steal(end)
        n = len(nums)
        return max(rob_range(0, n - 2), rob_range(1, n - 1))

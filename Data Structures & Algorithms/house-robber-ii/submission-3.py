class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def rob_range(start: int, end: int) -> int:
            memo = {}
            def steal(i: int) -> int:
                # Base cases
                if i < start:
                    return 0
                if i == start:
                    return nums[start]
                
                # Check cache
                if i in memo:
                    return memo[i]
                    
                # Store and return
                memo[i] = max(steal(i - 1), steal(i - 2) + nums[i])
                return memo[i]
                
            return steal(end)

        n = len(nums)
        # Max of (Index 0 to N-2) OR (Index 1 to N-1)
        return max(rob_range(0, n - 2), rob_range(1, n - 1))

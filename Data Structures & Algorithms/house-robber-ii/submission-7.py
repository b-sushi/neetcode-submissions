class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        def rob_linear(houses: list[int]) -> int:
            memo = {}
            def helper(i: int) -> int:
                if i < 0:
                    return 0
                if i == 0:
                    return houses[0]
                if i in memo:
                    return memo[i]

                memo[i] = max(helper(i - 1), helper(i - 2) + houses[i])
                return memo[i]

            return helper(len(houses) - 1)

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
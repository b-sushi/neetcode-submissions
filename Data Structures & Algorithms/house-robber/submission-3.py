#top down memoization

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def steal(n):
            if n== 0:
                return nums[0]
            if n==1:
                return max(nums[0], nums[1])
            if n in memo:
                return memo[n]
            else:
                memo[n] = max(steal(n-1), steal(n-2) + nums[n])
                return memo[n]
        return steal(len(nums) - 1)
        
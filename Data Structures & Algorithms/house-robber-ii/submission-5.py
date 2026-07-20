class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) -1
        if n ==0:
            return nums[0]
        def steal(n, restrict, memo):
            if n == restrict:
                return 0
            if n== 0:
                return nums[0]
            if n==1:
                return max(steal(0, restrict, memo), nums[1])
            if n in memo:
                return memo[n]
            else:
                memo[n] = max(steal(n-1, restrict, memo), steal(n-2, restrict, memo) + nums[n])
                return memo[n]
        return max(steal(n-1, n, {}), steal(n, 0, {}))
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memo = [0] * len(nums) 
        inverse = [0] * len(nums)
        for x in range(len(nums)):
            if x == 0:
                memo[0] = nums[0]
                inverse[0] = nums[0]
            else:
                memo[x] = max(memo[x-1] * nums[x], nums[x], inverse[x-1] * nums[x])
                inverse[x] = min(memo[x-1] * nums[x], nums[x], inverse[x-1] * nums[x])
        return max(memo)

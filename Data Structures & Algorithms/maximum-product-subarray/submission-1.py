class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        global_max = nums[0]
        for x in range(len(nums)):
            if x == 0:
                continue
            else:
                temp = curr_max
                curr_max = max(curr_max * nums[x], nums[x], curr_min * nums[x])
                curr_min = min(curr_min * nums[x], nums[x], temp * nums[x])
                global_max = max(curr_max, global_max)
        return global_max
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array = [1] * len(nums)
        right_array = [1] * len(nums)
        left_prod = 1
        right_prod = 1
        for i in range(len(nums)):
            left_array[i] = left_prod
            left_prod *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            right_array[i] = right_prod
            right_prod *= nums[i]
        return [i * j for i, j  in zip(left_array, right_array)]
        
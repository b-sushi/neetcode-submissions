class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        while L < R:
            M = (L+R) //2
            if nums[L] <= nums[M] <= nums[R]:
                #this is unrotated
                return nums[L]
            elif nums[L] > nums[R] > nums[M]:
                R = M
                #this means lowest number between L and M 
            else:
                L = M + 1
                #this means lowest between M and R
        return nums[L]

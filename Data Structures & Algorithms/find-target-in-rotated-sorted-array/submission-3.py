class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            M = (L+ R) // 2
            if nums[M] == target: return M
            #If middle is greater than rightmost, the minimum must be in the right half
            if nums[M] > nums[R]:

                #If our target is between M and R, it must be on the left, otherwise
                #-its on the right
                if nums[L] <= target < nums [M]:
                    R = M - 1
                else:
                    L = M+1
            #Otherwise the minimum is the left half
            else:
                #Means that the target is on the right
                if nums[R] >= target > nums [M]:
                    L = M + 1
                else:
                    R = M-1
        return -1
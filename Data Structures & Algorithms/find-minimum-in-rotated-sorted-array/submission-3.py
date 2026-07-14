class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        
        while L < R:
            M = (L + R) // 2

            # If middle element is greater than the rightmost element,
            # the minimum must be in the right half.
            if nums[M] > nums[R]:
                L = M + 1
            # Otherwise, the minimum is in the left half (including M)
            else:
                R = M
                
        return nums[L]
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 1
        maximum = 1
        if not nums:
            return 0
        for i, number in enumerate(s):
            if number - 1 not in s:
                longest = 1
                run = 1
                while number + run in s:
                    longest += 1
                    maximum = max(longest, maximum)
                    run += 1
        return maximum
                

            


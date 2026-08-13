class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        dupes = set()
        for n in nums:
            dupes.add(n)
        if len(nums) == len(dupes):
            return False
        else:
            return True
        
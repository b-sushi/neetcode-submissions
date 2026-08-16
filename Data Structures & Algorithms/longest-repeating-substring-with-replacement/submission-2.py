class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        l = 0
        longest = 1
        r = 0
        count = Counter()
        while r < len(s):
            count[s[r]] +=1
            while (r-l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l +=1
            longest = max(longest, r - l + 1)
            r +=1
        return longest

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, longest = 0, 0
        n = len(s)
        counts = [0] * 26
        length = 1
        for r in range(n):
            counts[ord(s[r]) - 65] += 1
            length = (r - l) + 1
            if (length) - max(counts) > k:
                counts[ord(s[l]) - 65] -= 1
                l +=1
            else:
                longest = max(length, longest)
        return longest
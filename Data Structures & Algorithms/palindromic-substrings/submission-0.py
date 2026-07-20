class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for x in range(len(s)):
            n = 0
            while x - n >= 0 and x + n < len(s) and s[x - n] == s[x + n]:
                count +=1
                n +=1
            n = 0
            while x - n >= 0 and x + n + 1< len(s) and s[x-n] == s[x + n + 1]:
                count +=1
                n +=1
        return count

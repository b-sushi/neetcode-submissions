class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        length = 1
        for x in range(len(s)):
            n = 1
            while x - n >= 0 and x + n < len(s) and s[x - n] == s[x + n]:
                if 2 * n + 1 >= length:
                    start = x - n
                    length = 2*n + 1
                n +=1
            n = 0
            while x - n >= 0 and x + n + 1 < len(s) and s[x + n + 1] == s[x -n]:
                if 2 * n +2>= length:
                    start = x - n
                    length = n * 2 + 2
                n +=1
        return s[start: start + length]

                    
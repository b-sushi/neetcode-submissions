#memoization

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def decode(n):
            if n == len(s):
                return 1
            if s[n] == '0':
                return 0
            if n in memo:
                return memo[n]
            else:
                if (n != len(s) - 1) and (s[n] == '1' or (s[n] == '2' and s[n+1] < '7')):
                    memo[n] = decode(n + 1) + decode(n+2)
                    return memo[n]
                else:
                    memo[n] = decode(n+1)
                    return memo[n]
        return decode(0)
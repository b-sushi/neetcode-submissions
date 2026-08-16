class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}
        for val in coins:
            memo[val] = 1
        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = float('inf')
                for c in coins:
                    if x - c >= 0:
                        memo[x] = min(memo[x], 1 + f(x-c))
                return memo[x]
        if f(amount) == float('inf'):
            return -1
        else:
            return f(amount)
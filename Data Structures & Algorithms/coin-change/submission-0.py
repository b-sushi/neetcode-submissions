# recursion
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float('inf')] * (1 + amount)
        memo[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if coin > i:
                    continue
                else:
                    memo[i] = min(memo[i], memo[i-coin] + 1)
        if memo[amount] == float('inf'):
            return -1
        else: 
            return memo[amount]

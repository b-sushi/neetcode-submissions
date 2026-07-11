class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {0: 0, 1:0}
        n = len(cost)
        def f(x):
            if x in memo:
                return memo[x]
            else:
                val1 = f(x-1) + cost[x-1]
                val2 = f(x-2) + cost[x-2]
                memo[x] = min(val1, val2)
                return memo[x]
        return f(n)
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_satisfied = sum(c for c, g in zip(customers, grumpy) if g==0)
        current_satisfied = sum(customers[i] for i in range(minutes) if grumpy[i] ==1)
        max_satisfied = current_satisfied
        for i in range(minutes, len(grumpy)):
            if grumpy[i] == 1:
                current_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                current_satisfied -= customers[i-minutes]
            max_satisfied = max(max_satisfied, current_satisfied)
        return max_satisfied + total_satisfied

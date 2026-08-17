class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights) 
        while l < r:
            M = (l + r) //2
            curr_weight = 0 
            curr_day = 1
            for weight in weights:
                if curr_weight > M:
                    curr_weight = weight
                    curr_day +=1
                curr_weight += weight
                if curr_weight > M:
                    curr_weight = weight
                    curr_day +=1
            if curr_day > days:
                l = M +1
            else:
                r = M
        return l
                
            


# pretty common pattern
# we know that the max capacity needed is the sum of weights, since we can load everything on
# we know that the fastest we need to do it will be the sum of weights
# we know that the lowest will be the maximum weight
# we then perform a binary search, we try a middle value and then we determine if it does it fast enough.
#if it does we then set R equal to M. we know that we dont need to do it faster than m
#if it is too slow we set L to above M, we know that M is invalid
# we continue searching until we settle on the best value. we test the best value and we'll set R to M and then it'll compute a new M and it'll set L to above the next M. eventually we'll have L and R on the same value
#to implement the actual sort my idea is to have a pointer that will go through the array. it'll basically just increment until the sum of the values so far are above M, it'll then add 1 to the days count and then it'll just keep going
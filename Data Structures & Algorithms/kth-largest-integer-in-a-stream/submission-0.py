class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.kth = []
        self.k = k
        heapq.heapify(self.kth)
        for x in nums:
            heapq.heappush(self.kth, x)
            if len(self.kth) > k:
                heapq.heappop(self.kth)

    def add(self, val: int) -> int:
        if len(self.kth) < self.k:
            heapq.heappush(self.kth, val)
            return self.kth[0]
        else:
            heapq.heappushpop(self.kth, val)
            return self.kth[0]

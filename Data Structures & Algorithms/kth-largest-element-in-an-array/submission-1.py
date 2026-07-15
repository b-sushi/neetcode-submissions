class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []

        for x in range(len(nums)):
            if len(heap) >= (k):
                heapq.heappushpop(heap,nums[x])
            else:
                heapq.heappush(heap, nums[x])
        return heap[0]
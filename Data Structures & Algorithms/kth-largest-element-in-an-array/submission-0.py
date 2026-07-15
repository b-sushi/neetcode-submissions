class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        heapq.heapify(heap)
        for x in range(len(nums)):
            if len(heap) >= (len(nums) - k + 1):
                heapq.heappushpop(heap,-nums[x])
            else:
                heapq.heappush(heap, -nums[x])
        return -heap[0]
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq

        heap = []
        heapq.heapify(heap)
        for x in range(len(points)):
            if len(heap) >= k:
                heapq.heappushpop(heap, (-((points[x][0]) ** 2 + (points[x][1]) ** 2), points[x]))
            else:
                heapq.heappush(heap, (-((points[x][0]) ** 2 + (points[x][1]) ** 2), points[x]))
        return [item[1] for item in heap]
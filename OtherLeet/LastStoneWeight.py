import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for s in stones:
            heapq.heappush(heap, -1*s)
        # print(heap)
        while len(heap) > 1:
            largest = -1*heapq.heappop(heap)
            slargest = -1*heapq.heappop(heap)
            if largest != slargest:
                heapq.heappush(heap, -1*(largest-slargest))
            # print(heap)
        if heap:
            return -1 * heap[0]
        else:
            return 0

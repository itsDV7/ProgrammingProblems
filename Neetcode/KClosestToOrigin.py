from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def compare(p1):
            return [(sqrt(p1[0]*p1[0] + p1[1]*p1[1])), p1]

        heap = list()
        for p in points:
            heapq.heappush(heap, compare(p))

        ans = list()
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans

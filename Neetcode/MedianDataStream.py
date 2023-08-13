import heapq
class MedianFinder:

    def __init__(self):
        self.maxheap = list()
        self.minheap = list()
        heapq.heapify(self.maxheap)
        heapq.heapify(self.minheap)

    def addNum(self, num: int) -> None:
        if not self.maxheap:
            heapq.heappush(self.maxheap, (-1 * num))
        else:
            if abs(len(self.maxheap) - len(self.minheap)) < 1:
                if num <= (-1 * self.maxheap[0]):
                    heapq.heappush(self.maxheap, (-1 * num))
                else:
                    heapq.heappush(self.minheap, num)
            else:
                if len(self.maxheap) > len(self.minheap):
                    if num <= (-1 * self.maxheap[0]):
                        heapq.heappush(self.minheap, (-1 * heapq.heappop(self.maxheap)))
                        heapq.heappush(self.maxheap, (-1 * num))
                    else:
                        heapq.heappush(self.minheap, num)
                else:
                    if num <= (-1 * self.maxheap[0]):
                        heapq.heappush(self.maxheap, (-1 * num))
                    else:
                        heapq.heappush(self.maxheap, (-1 * heapq.heappop(self.minheap)))
                        heapq.heappush(self.minheap, num)

    def findMedian(self) -> float:
        if not abs(len(self.minheap) - len(self.maxheap)):
            return ((-1 * self.maxheap[0]) + self.minheap[0])/2
        else:
            if len(self.maxheap) > len(self.minheap):
                return (-1 * self.maxheap[0])
            else:
                return self.minheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

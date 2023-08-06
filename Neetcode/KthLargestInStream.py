class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        for i in range(len(self.heap), -1, -1):
            self._siftdown(i)

    def _siftup(self, index):
        parent = (index-1)//2
        if parent >= 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._siftup(parent)

    def _siftdown(self, index):
        swap = index
        left = (2*index) + 1
        right = (2*index) + 2

        if left < len(self.heap) and self.heap[left] < self.heap[swap]:
            swap = left
        if right < len(self.heap) and self.heap[right] < self.heap[swap]:
            swap = right

        if swap != index:
            self.heap[index], self.heap[swap] = self.heap[swap], self.heap[index]
            self._siftdown(swap)

    def add(self, val: int) -> int:
        self.heap.append(val)
        self._siftup(len(self.heap)-1)
        while self.heap and len(self.heap) > self.k:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            self.heap.pop()
            self._siftdown(0)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

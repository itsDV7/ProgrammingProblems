class MaxHeap:
    def __init__(self):
        self.heap = list()
    
    def insert(self, value):
        self.heap.append(value)
        self._siftup(len(self.heap) - 1)

    def _siftup(self, index):
        value = self.heap[index]
        while index and self.heap[((index + 1) // 2) - 1] < value:
            self.heap[index] = self.heap[((index + 1) // 2) - 1]
            self.heap[((index + 1) // 2) - 1] = value
            index = ((index + 1) // 2) - 1

    def getmax(self):
        if self.heap:
            return self.heap[0]
        else:
            return None
    
    def extractmax(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        else:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            maxelem = self.heap.pop()
            self._siftdown(0)
            return maxelem

    def _siftdown(self, index):
        value = self.heap[index]
        while True:
            left_index = 2*(index + 1) - 1
            right_index = 2*(index + 1)
            if left_index < len(self.heap):
                if right_index < len(self.heap):
                    if self.heap[left_index] >= self.heap[right_index]:
                        if value < self.heap[left_index]:
                            self.heap[index] = self.heap[left_index]
                            self.heap[left_index] = value
                            index = left_index
                        else:
                            break
                    else:
                        if value < self.heap[right_index]:
                            self.heap[index] = self.heap[right_index]
                            self.heap[right_index] = value
                            index = right_index
                        else:
                            break
                else:
                    if value < self.heap[left_index]:
                        self.heap[index] = self.heap[left_index]
                        self.heap[left_index] = value
                        index = left_index
                    else:
                        break
            else:
                break

    def changepriority(self, ofvalue, tovalue):
        for i, h in enumerate(self.heap):
            if h == ofvalue:
                index = i
                break
        else:
            return

        self.heap[index] = tovalue
        
        self._siftup(index)
        self._siftdown(index)

    def remove(self, value):
        for i, h in enumerate(self.heap):
            if h == value:
                index = i
                break
        else:
            return

        self.heap[index], self.heap[-1] = self.heap[-1], self.heap[index]
        self.heap.pop()

        self._siftup(index)
        self._siftdown(index)

    def heapify(self, arr):
        for i, a in enumerate(arr):
            self.insert(a)

    def _print(self):
        print(self.heap)
        

# arr = [42, 7, 11, 14, 18, 13, 18, 12, 19, 30]

# maxheap = MaxHeap()
# maxheap.heapify(arr)
# maxheap.changepriority(30, 25)
# maxheap.changepriority(7, 6)
# maxheap.changepriority(42, 45)
# maxheap.changepriority(12, 50)
# maxheap.remove(18)
# while maxheap.getmax():
#     print(maxheap.extractmax())


# 50
# 45
# 25
# 19
# 18
# 14
# 13
# 11
# 6

class MinHeap:
    
    def __init__(self):
        self.heap = list()
        
    def insert(self, pair):
        self.heap.append(pair)
        if self.heap:
            self._siftup(len(self.heap)-1)
    
    def _siftup(self, index):
        parent = (index-1)//2
        if parent >= 0:
            if self.heap[parent][1] > self.heap[index][1]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
                self._siftup(index)
            if self.heap[parent][1] == self.heap[index][1] and \
            self.heap[parent][0] > self.heap[index][0]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
                self._siftup(index)
        else:
            return
        
    def extractmin(self):
        if self.heap:
            minval = self.heap[0]
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            self.heap.pop()
            self._siftdown(0)
            return minval
        else:
            return None
    
    def _siftdown(self, index):
        left_child = 2*index + 1
        right_child = 2*index + 2
        swap_index = None
        
        if left_child < len(self.heap) and self.heap[left_child][0] == None \
        and self.heap[left_child][1] < self.heap[index][1]:
            swap_index = left_child
        if right_child < len(self.heap) and self.heap[right_child][0] == None \
        and self.heap[right_child][1] < self.heap[index][1] \
        and self.heap[right_child][1] < self.heap[left_child][1]:
            swap_index = right_child
            
        if left_child < len(self.heap) and self.heap[left_child][0] != None \
        and self.heap[left_child][1] < self.heap[index][1]:
            swap_index = left_child
        if right_child < len(self.heap) and self.heap[right_child][0] != None \
        and self.heap[right_child][1] < self.heap[index][1] \
        and self.heap[right_child][1] <= self.heap[left_child][1]:
            if self.heap[right_child][1] == self.heap[left_child][1] \
            and self.heap[right_child][0] < self.heap[left_child][0]:
                swap_index = right_child
            if self.heap[right_child][1] < self.heap[left_child][1]:
                swap_index = right_child
            
        if left_child < len(self.heap) and self.heap[left_child][0] != None \
        and self.heap[left_child][1] == self.heap[index][1] \
        and self.heap[left_child][0] < self.heap[index][0]:
            swap_index = left_child
        if right_child < len(self.heap) and self.heap[right_child][0] != None \
        and self.heap[right_child][1] == self.heap[index][1] \
        and self.heap[right_child][0] < self.heap[index][0] \
        and self.heap[right_child][1] <= self.heap[left_child][1]:
            if self.heap[right_child][1] == self.heap[left_child][1] \
            and self.heap[right_child][0] < self.heap[left_child][0]:
                swap_index = right_child
            if self.heap[right_child][1] < self.heap[left_child][1]:
                swap_index = left_child
        
        if swap_index:
            self.heap[index], self.heap[swap_index] = self.heap[swap_index], self.heap[index]
            index = swap_index
            self._siftdown(index)
        else:
            return
    
    def getmin(self):
        if self.heap:
            return self.heap[0]
        else:
            return None
        
    def _print(self):
        print(self.heap)

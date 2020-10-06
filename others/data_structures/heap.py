



'''
Max Heap
'''

class MaxHeap:
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = [None] * self.maxsize
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('The heap is full!')

        self._elements[self._count] = value
        self._count += 1
        # to maintain the heap
        self._siftup(self._count-1)

    def _siftup(self, idx):
        if idx > 0:
            parent = (idx-1) // 2
            # swap if the inserted value larger than the partent
            if self._elements[idx] > self._elements[parent]:
                self._elements[idx], self._elements[parent] = self._elements[parent], self._elements[idx]
                self._siftup(parent)
    
    def extract(self):
        if self._count <= 0:
            raise Exception("The heap is empty!")
        
        # keep the root value
        value = self._elements[0]
        self._count -= 1
        # swap the last item to the root and then sift down
        self._elements[0] = self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self, idx):
        left = 2 * idx + 1
        right = 2 * idx + 2

        # determine which node contains the larger value
        largest = idx

        # check if left root exist and greater than root
        if left < self._count and self._elements[left] > self._elements[largest]:
            largest = left
        
        # check if right root exist and greater than root
        if right < self._count and self._elements[right] > self._elements[largest]:
            largest = right
        
        # if the largest being changed, swap it with the root
        if largest != idx:
            self._elements[idx], self._elements[largest] = self._elements[largest], self._elements[idx]
            # heapify the root
            self._siftdown(largest)


class MinHeap:
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = [None] * maxsize
        self._count = 0
    
    def __len__(self):
        return self._count
    
    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception("The heap is full!")
        
        # add the new element to the end
        self._elements[self._count] = value
        self._count += 1
        # maintian the heap
        self.siftup(self._count-1)

    def siftup(self, idx):
        if idx > 0:
            parent = (idx - 1) // 2
            # swap if the parent larger than the idx
            if self._elements[parent] > self._elements[idx]:
                self._elements[parent], self._elements[idx] = self._elements[idx], self._elements[parent]
                self.siftup(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception("The heap is empty!")
        # keep the root
        value = self._elements[0]
        # swap the root to the end
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        # maintian the heap
        self._siftdown(0)
        return value

    def _siftdown(self, idx):
        left = 2 * idx + 1
        right = 2 * idx + 2

        # determine which node contains the smaller value
        smallest = idx

        # check if left root exist and smaller than root
        if left < self._count and self._elements[left] < self._elements[smallest]:
            smallest = left

        # check if right root exist and smaller than root
        if right < self._count and self._elements[right] < self._elements[smallest]:
            smallest = right
        
        # if the smallest being changed, swap it with the root
        if smallest != idx:
            self._elements[idx], self._elements[smallest] = self._elements[smallest], self._elements[idx]
            # heapify the rootss
            self._siftdown(smallest)

def test_maxheap():
    import random
    n = 5
    h = MaxHeap(n)
    for i in range(n):
        h.add(i)
    
    for i in reversed(range(n)):
        out = h.extract()
        assert i == out
        print(out)

def test_minheap():
    import random
    n = 10
    h = MinHeap(n)
    for i in reversed(range(n)):
        h.add(i)
    
    for i in range(n):
        out = h.extract()
        assert i == out
        print(out)


if __name__ == "__main__":
    test_maxheap()
    test_minheap()
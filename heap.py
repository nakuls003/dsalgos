class Heap:

    def __init__(self, a = None):
        self._a = [] if a is None else a
        self.build_maxheap()

    def __len__(self):
        return len(self._a)

    def build_maxheap(self):
        for i in range(len(self)-1, -1, -1):
            self.max_heapify(i, len(self))

    def max_heapify(self, i, n):
        left = 2*i+1
        right = 2*i+2
        if left < n and self._a[left] > self._a[i]:
            largest = left
        else:
            largest = i
        if right < n and self._a[right] > self._a[largest]:
            largest = right
        if largest != i:
            self._a[largest], self._a[i] = self._a[i], self._a[largest]
            self.max_heapify(largest, n)

    def insert(self, val):
        self._a.append(val)
        i = len(self)-1
        while i > 0 and self._a[(i-1)/2] < self._a[i]:
            self._a[(i-1)/2], self._a[i] = self._a[i], self._a[(i-1)/2]
            i = (i-1)/2

    def first(self):
        return self._a[0]

    def return_first(self):
        ret = self._a[0]
        self._a[0] = self._a[len(self)-1]
        self._a.pop()
        self.max_heapify(0, len(self))
        return ret
    
def heapsort(a):
    h = Heap(a)
    for i in range(len(a)-1, 0, -1):
        h._a[0], h._a[i] = h._a[i], h._a[0]
        h.max_heapify(0, i)

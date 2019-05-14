class MinPriorityQueue:

    def __init__(self, arr = None):
        self._arr = [] if arr is None else arr
        self._map = {item[0]: idx for idx, item in enumerate(self._arr)}
        self._build_minheap()

    def __len__(self):
        return len(self._arr)

    def _build_minheap(self):
        for i in range(len(self)-1, -1, -1):
            self._min_heapify(i)

    def _min_heapify(self, i):
        left, right = 2*i+1, 2*i+2
        smallest = i
        if left < len(self) and self._arr[left][1] < self._arr[smallest][1]:
            smallest = left
        if right < len(self) and self._arr[right][1] < self._arr[smallest][1]:
            smallest = right
        if smallest != i:
            self._map[self._arr[i][0]] = smallest
            self._map[self._arr[smallest][0]] = i
            self._arr[i], self._arr[smallest] = self._arr[smallest], self._arr[i]

    def insert(self, key, val):
        self._arr.append((key, val))
        i = len(self)-1
        self._map[key] = i
        while i > 0 and self._arr[i][1] < self._arr[(i-1)//2][1]:
            self._map[self._arr[i][0]] = (i-1)//2
            self._map[self._arr[(i-1)//2][0]] = i
            self._arr[i], self._arr[(i-1)//2] = self._arr[(i-1)//2], self._arr[i]
            i = (i-1)//2

    def get_val(self, key):
        return self._arr[self._map[key]][1]

    def extract_min(self):
        ret = self._arr[0]
        self._arr[0] = self._arr[-1]
        del self._map[ret[0]]
        self._arr.pop()
        self._min_heapify(0)
        return ret

    def __contains__(self, item):
        return item in self._map

    def decrease(self, key, new_val):
        i = self._map[key]
        self._arr[i][1] = new_val
        while i > 0 and self._arr[i][1] < self._arr[(i-1)//2][1]:
            self._map[self._arr[i][0]] = (i-1)//2
            self._map[self._arr[(i-1)//2][0]] = i
            self._arr[i], self._arr[(i-1)//2] = self._arr[(i-1)//2], self._arr[i]
            i = (i-1)//2

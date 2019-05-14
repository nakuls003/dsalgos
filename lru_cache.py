class LRUCache:
    class ListNode:
        def __init__(self, k, v):
            self.k = k
            self.v = v
            self.prev = None
            self.next = None

    # @param capacity, an integer
    def __init__(self, capacity):
        self._map = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    # @return an integer
    def get(self, key):
        if key not in self._map:
            return -1
        node = self._map[key]
        value = node.v
        if node != self.head:
            predecessor, successor = node.prev, node.next
            predecessor.next = successor
            if successor:
                successor.prev = predecessor
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node
        return value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        node = self.ListNode(key, value)
        self._map[key] = node
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        if len(self._map) > self.capacity:
            del self._map[self.tail.k]
            predecessor = self.tail.prev
            predecessor.next = None
            self.tail = predecessor

if __name__ == '__main__':
    l = LRUCache(1)
    l.set(2, 1)
    print(l.get(2))
    l.set(3, 2)
    print(l.get(2))
    print(l.get(3))
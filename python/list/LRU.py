class LRUNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = LRUNode(0, 0)
        self.tail = LRUNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0
        self.content = {}

    def move2head(self, node):

        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node


    # @return an integer
    def get(self, key):
        if key in self.content:
            t = self.content[key]
            self.move2head(t)
            return t.val
        return -1


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.content:
            self.content[key].val = value
            self.move2head(self.content[key])
            return


        if self.count >= self.capacity:
            t = self.tail.prev
            t.next.prev = t.prev
            t.prev.next = t.next
            self.count -= 1
            del self.content[t.key]
        t = LRUNode(key, value)
        self.head.next.prev = t
        t.next = self.head.next
        t.prev = self.head
        self.head.next = t
        self.count += 1
        self.content[key] = t


t = LRUCache(1)
t.set(2,1)
print t.get(2)
t.set(3,2)
print t.get(2)
print t.get(3)




import heapq

class MedianFinder:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []
        self.minn = 0
        self.maxn = 0

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if self.maxn + self.minn == 0:
            self.minn += 1
            heapq.heappush(self.minheap, num)
        elif self.maxn < self.minn:
            self.maxn += 1
            if num <= self.minheap[0]:
                heapq.heappush(self.maxheap, -num)
            else:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
                heapq.heappush(self.minheap, num)
        elif self.minn < self.maxn:
            self.minn += 1
            if num >= -self.maxheap[0]:
                heapq.heappush(self.minheap, num)
            else:
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
                heapq.heappush(self.maxheap, -num)
        else:
            if num < -self.maxheap[0]:
                self.maxn += 1
                heapq.heappush(self.maxheap, - num)
            else:
                self.minn += 1
                heapq.heappush(self.minheap, num)


    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.maxn == self.minn and self.maxheap:
            return (self.minheap[0] - self.maxheap[0])/2.0
        if self.maxn > self.minn:
            return -self.maxheap[0]
        if self.minn > self.maxn:
            return self.minheap[0]


# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
mf.addNum(3)
mf.addNum(4)
print mf.findMedian()
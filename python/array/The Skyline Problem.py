import heapq

class Solution:

    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):

        remain = {}
        result = []

        for i in xrange(len(buildings)):
            left, right, height = buildings[i]
            if right not in remain or remain[right] < height:
                remain[right] = height

            countthis = True
            for x in remain:
                if remain[x] > height:
                    # which means the left is covered by former buildings.
                    countthis = False
                    break
            if countthis:
                if not result or height != result[-1][1]:
                    result.append([left, height])

            for x in remain:
                if x <= left:
                    del remain[x]




a = 'abc'
a[0] = 'o'
print a
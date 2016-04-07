import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        corners = set([b[0] for b in buildings] + [b[1] for b in buildings])
        corners = sorted(list(corners))

        live = []
        i = 0

        skyline = [[0, -1]]

        for c in corners:

            while i < len(buildings) and buildings[i][0] <= c:
                heapq.heappush(live, (-buildings[i][2], buildings[i][1]))
                i += 1

            while live and live[0][1] <= c:
                heapq.heappop(live)

            if live:
                h = -live[0][0]
            else:
                h = 0

            if h != skyline[-1][1]:
                skyline.append([c, h])

        return skyline[1:]




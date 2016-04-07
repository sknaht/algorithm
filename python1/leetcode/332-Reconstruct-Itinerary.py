class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        n = len(tickets)
        g = [[0] * (n + 1) for i in xrange(n + 1)]

        cities = {}
        k = 0
        for start, end in tickets:
            if start not in cities:
                cities[start] = k
                k += 1
            if end not in cities:
                cities[end] = k
                k += 1

            g[cities[start]][cities[end]] += 1

        cities_sorted = sorted(cities.keys())

        ans = []

        def dfs(path, result):

            if len(path) > n:
                for x in path:
                    result.append(x)
                return

            start = cities[path[-1]]

            for city in cities_sorted:
                citynumber = cities[city]
                if g[start][citynumber] > 0:
                    g[start][citynumber] -= 1
                    dfs(path + [city], result)
                    if result:
                        return
                    g[start][citynumber] += 1

        dfs(["JFK"], ans)
        return ans


if __name__ == "__main__":
    t = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    print Solution().findItinerary(t)

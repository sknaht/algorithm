class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        graph = {i : set() for i in xrange(n)}
        degree = {i : 0 for i in xrange(n)}
        for s, e in edges:
            graph[s].add(e)
            graph[e].add(s)
            degree[s] += 1
            degree[e] += 1

        current = [i for i in xrange(n) if degree[i] <= 1]
        result = []

        while current:
            next = []
            result = current[:]
            for i in current:
                for j in graph[i]:
                    degree[j] -= 1
                    if degree[j] == 1:
                        next.append(j)
            current = next
        return result


print Solution().findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])




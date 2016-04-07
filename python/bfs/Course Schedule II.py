class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):

        graph, degree = {x: [] for x in xrange(numCourses)}, {x: 0 for x in xrange(numCourses)}
        for p in prerequisites:
            graph[p[1]].append(p[0])
            degree[p[0]] += 1

        curr, result = [], []
        for x in degree:
            if degree[x] == 0:
                curr.append(x)
                result.append(x)

        while curr:
            next = []
            for x in curr:
                for d in graph[x]:
                    if d in result:
                        return []
                    degree[d] -= 1
                    if degree[d] == 0:
                        next.append(d)
                        result.append(d)
            curr = next

        if len(result) == numCourses:
            return result
        return []

print Solution().findOrder(2, [[1,0]])



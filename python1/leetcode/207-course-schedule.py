class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        prerq = [[] for i in xrange(numCourses)]
        num = [0 for i in xrange(numCourses)]
        for (i, j) in prerequisites:
            prerq[j].append(i)
            num[i] += 1

        curr = []
        for i in xrange(numCourses):
            if num[i] == 0:
                curr.append(i)

        while curr:
            next = []
            for i in curr:
                for j in prerq[i]:
                    num[j] -= 1
                    if num[j] == 0:
                        next.append(j)
            curr = next
        for i in xrange(numCourses):
            if num[i] > 0:
                return False
        return True


    def canFinish1(self, numCourses, prerequisites):
        edges = {i: set([]) for i in xrange(numCourses)}
        for (i, j) in prerequisites:
            edges[j].add(i)

        def containCycle(node, path):
            if not edges[node]:
                return False

            for i in list(edges[node]):
                if i in path:
                    return True
                edges[node].remove(i)
                if containCycle(i, path + [i]):
                    return True
            return False

        for i in xrange(numCourses):
            if containCycle(i, [i]):
                return False
        return True


print Solution().canFinish1(2, [[1,0], [0,1]])
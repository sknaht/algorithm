class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def traceback(result, n, k, index, path):
            if len(path) >= k:
                result.append([x for x in path])
                return
            for i in xrange(index, n + 1):
                traceback(result, n, k, i + 1, path + [i])

        result = []
        traceback(result, n, k, 1, [])
        return result


print Solution().combine(4, 2)
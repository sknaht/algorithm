class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations, reverse=True)
        for i in xrange(len(citations)):
            if citations[i] < i:
                break
        return i

print Solution().hIndex([3, 0, 6, 1, 5])
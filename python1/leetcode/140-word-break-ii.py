class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """

        trace = {i: [] for i in xrange(len(s))}
        m = 0
        for w in wordDict:
            m = max(m, len(w))

        able = [False for i in xrange(len(s) + 1)]
        able[0] = True
        for i in xrange(len(s)):
            if able[i]:
                for j in xrange(m):
                    if j + i + 1 > len(s):
                        break
                    if s[i: j + i + 1] in wordDict:
                        trace[i].append(i + j + 1)
                        able[i + j + 1] = True

        def traceback(result, trace, index, path, end, s):
            if index >= end:
                result.append(' '.join(path))
                return
            for i in trace[index]:
                traceback(result, trace, i, path + [s[index: i]], end, s)

        result = []
        if able[len(s)]:
            traceback(result, trace, 0, [], len(s), s)
        return result





class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """

        found = False
        wordlist.union([beginWord, endWord])

        visited = set([])
        trace = {word: [] for word in wordlist}

        curr = {beginWord}
        while not found and curr:
            for word in curr:
                visited.add(word)
            next = set([])
            for word in curr:
                for i in xrange(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + c + word[i + 1:]
                        if candidate not in visited and candidate in wordlist:
                            next.add(candidate)
                            trace[candidate].append(word)
                            if candidate == endWord:
                                found = True
            curr = next

        ans = []
        if found:
            self.traceback(ans, endWord, trace, [])
        return ans

    def traceback(self, ans, word, trace, path):
        if not trace[word]:
            ans.append([word] + path)
            return
        for prev in trace[word]:
            self.traceback(ans, prev, trace, [word] + path)

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):

        self.solutions = [[] for i in xrange(len(s))]
        for i in xrange(len(s)):
            if s[:i+1] in dict: self.solutions[i].append(0)
            for j in xrange(i):
                if self.solutions[j] and s[j+1:i+1] in dict:
                    self.solutions[i].append(j+1)
        self.result = []
        self.findpath([], len(s)-1)
        res = []
        for sol in self.result:
            res.append(' '.join(s[sol[i-1]+1:sol[i]+1] for i in xrange(1, len(sol))))
        return res

    def findpath(self, path, index):
        if index == -1:
            self.result.append([-1] + path[::-1])
            return True
        for x in self.solutions[index]:
            self.findpath(path + [index], x-1)

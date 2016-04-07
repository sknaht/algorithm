"""
 Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

    Only one letter can be changed at a time
    Each intermediate word must exist in the dictionary

For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

Return

  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]

Note:

    All words have the same length.
    All words contain only lowercase alphabetic characters.

"""

"""
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        self.result = {}
        self.minstep = 100000
        self.find(start, end, list(dict) + [end], [start], 0)

        print self.result
        if not self.result:
            return []
        return self.result[self.minstep]

    def find(self, start, end, dict, tmp, step):
        if step > self.minstep:
            return
        if start == end:
            if step < self.minstep:
                self.minstep = step
            if step not in self.result:
                self.result[step] = [[_ for _ in tmp]]
            else:
                self.result[step].append([_ for _ in tmp])
            return

        cand = []
        for c in 'abcdefghijklmnopqrstuvwxyz':
            for i in xrange(len(start)):
                w = start[:i] + c + start[i+1:]
                if w in dict and w not in tmp:
                    cand.append(w)
        cand.sort(key = lambda w: self.diff(w, end))
        for w in cand:
            self.find(w, end, dict, tmp + [w], step + 1)

    def diff(self, w1, w2):
        r = 0
        for i in xrange(len(w1)):
            if w1[i] != w2[i]:
                r += 1
        return r
"""

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        visited = set([])
        current = set([start])
        found = False
        dict.add(end)
        dict.add(start)
        trace = {word: [] for word in dict}

        while not found and current:
            for word in current:
                visited.add(word)

            next = set([])
            for word in current:
                for i in xrange(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + c + word[i + 1: ]
                        if candidate not in visited and candidate in dict:
                            trace[candidate].append(word)
                            next.add(candidate)
                        if candidate == end:
                            found = True
            current = next
        result = []
        if found:
            self.backtrack(result, trace, end, [])
        return result

    def backtrack(self, result, trace, word, path):
        if not trace[word]:
            result.append([word] + path)
            return
        for previous in trace[word]:
            self.backtrack(result, trace, previous, [word] + path)


print Solution().findLadders("qa", "sq", set(["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))

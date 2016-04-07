class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):

        r = []
        curr = 0
        line = []
        for w in words:
            if len(w) + curr > L and line:
                emps = L - curr + len(line)
                i = 0
                while emps>0:
                    line[i] += ' '
                    emps -= 1
                    i += 1
                    if i >= len(line)-1:
                        i = 0
                r.append(''.join(line))
                line = []
                curr = 0

            line.append(w)
            curr += 1 + len(w)
        if line:
            emps = L - curr + len(line) + 1
            line[-1] += ' '*emps
            r.append(' '.join(line))

        return r



t = Solution()
print t.fullJustify(["What","must","be","shall","be."], 12)
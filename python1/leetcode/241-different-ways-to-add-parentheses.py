
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        ops = ('+', '-', '*')
        s = []
        t = 0
        for c in input:
            if c in ops:
                s.append(t)
                s.append(c)
                t = 0
            else:
                t = t * 10 + int(c)
        s.append(t)
        if len(s) == 1:
            return s

        result = []

        def calculate(left, opt, right):
            rl, rr = [], []
            if len(left) == 1:
                rl = [left[0]]
            else:
                for i in xrange(1, len(left)):
                    if left[i] in ops:
                        rl.extend(calculate(left[:i], left[i], left[i + 1:]))
            if len(right) == 1:
                rr = [right[0]]
            else:
                for i in xrange(1, len(right)):
                    if right[i] in ops:
                        rr.extend(calculate(right[:i], right[i], right[i + 1:]))

            res = []
            for l in rl:
                for r in rr:
                    if opt == '+':
                        res.append(l + r)
                    if opt == '-':
                        res.append(l - r)
                    if opt == '*':
                        res.append(l * r)
            return res

        for i in xrange(len(s)):
            if s[i] in ops:
                result.extend(calculate(s[:i], s[i], s[i + 1:]))

        return result


print Solution().diffWaysToCompute('11')
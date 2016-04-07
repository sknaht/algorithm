class Solution(object):
    def removeDuplicateLetters(self, s):

        p = {c: i for i, c in enumerate(s)}
        result = []
        already = set([])

        for i, c in enumerate(s):
            if not result or (c not in already):
                while result:
                    if c < result[-1] and p[result[-1]] > i:
                        already.remove(result.pop())
                    else:
                        break
                result.append(c)
                already.add(c)

        return ''.join(result)


print Solution().removeDuplicateLetters('cbacdcbc')


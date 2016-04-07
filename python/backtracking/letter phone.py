class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if not digits:
            return []

        map = [' ', '', 'abc', 'def', 'ghi','jkl','mno','pqrs','tuv','wxyz']
        result = []

        def bt(curr, i):
            if i >= len(digits):
                result.append(curr)
                return

            for c in map[ord(digits[i]) - ord('0')]:
                bt(curr + c, i + 1)

        bt('', 0)
        return result


print Solution().letterCombinations('')
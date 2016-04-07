class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        def change_to_bit(word):
            bit = 0
            for c in set(word):
                bit |= 1 << (ord(c) - ord('a'))
            return bit

        bits = map(change_to_bit, words)

        result = 0
        for i in xrange(len(words)):
            for j in xrange(i + 1, len(words)):
                if bits[i] & bits[j] == 0:
                    result = max(result, len(words[i]) * len(words[j]))

        return result


t = Solution().maxProduct(["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"])
print t
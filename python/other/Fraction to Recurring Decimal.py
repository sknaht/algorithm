class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        if numerator * denominator < 0:
            minus = True
        else:
            minus = False
        numerator = abs(numerator)
        denominator = abs(denominator)

        large, numerator = numerator / denominator, numerator % denominator
        if numerator == 0:
            if minus:
                return '-' + str(large)
            return str(large)

        sequence = [numerator]
        result = []
        repeatlen = 0
        while numerator > 0:
            numerator *= 10
            t, numerator = numerator / denominator, numerator % denominator
            result.append(t)
            if numerator not in sequence:
                sequence.append(numerator)
            else:
                i = len(sequence) - 1
                while i >= 0:
                    if numerator == sequence[i]:
                        break
                    i -= 1
                repeatlen = len(sequence) - i
                break

        t = str(large) + '.'
        if repeatlen == 0:
            for c in result:
                t += chr(ord('0') + c)
        else:
            for i in xrange(len(sequence) - repeatlen):
                t += chr(ord('0') + result[i])
            t += '('
            for i in xrange(len(sequence) - repeatlen, len(sequence)):
                t += chr(ord('0') + result[i])
            t += ')'
        if minus:
            return '-' + t
        return t


print Solution().fractionToDecimal(50, 928232)
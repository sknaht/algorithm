"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):

        def add(n1, n2):
            if len(n1) > len(n2):
                return add(n2, n1)
            t = [0] * (len(n2) + 1)
            carry = 0
            for i in xrange(len(n1)):
                t[i] = n1[i] + n2[i] + carry
                t[i], carry = t[i] % 10, t[i] / 10
            for i in xrange(len(n1), len(n2)):
                t[i] = n2[i] + carry
                t[i], carry = t[i] % 10, t[i] / 10
            t[len(n2)] = carry
            return t

        def mult(n1, n):
            if n == 0:
                return [0]
            if n == 1:
                return [_ for _ in n1]
            carry = 0
            t = [0] * (len(n1) + 1)
            for i in xrange(len(n1)):
                x  = n1[i] * n  + carry
                t[i], carry = x % 10, x / 10
            t[len(n1)] = carry
            return t

        num1 = [int(x) for x in num1]
        num2 = [int(x) for x in num2]
        num1.reverse()
        num2.reverse()
        result = [0]
        for n in num1:
            t = mult(num2, n)
            result = add(result, t)
            num2.insert(0, 0)

        return ''.join(reversed([str(x) for x in result])).lstrip('0') or '0'


print Solution().multiply('1092731', '319230')




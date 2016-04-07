class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        a = [int(c) for c in num]
        n = len(a)

        def ok(start, l1, l2, l3):
            if a[start + l1 + l2] == 0:
                return False
            """
            carry = 0
            i, j, k = l1, l2, l3
            while carry or i > 0 or j > 0:
                x = a[start + i - 1] + a[start + l1 + j - 1] + carry
                carry = x / 10
                if k <= 0 or x % 10 != a[start + l1 + l2 + k - 1]:
                    return False
                i -= 1
                j -= 1
                k -= 1
            return True
            """
            return int(num[start: start + l1]) + int(num[start + l1 : start + l1 + l2]) == int(num[start + l1 + l2: start + l1 + l2 + l3])


        def valid(l1, l2):
            if max(l1, l2) > n - l1 - l2 or a[l1 + l2] == 0:
                return False
            start, end = 0, l1 + l2
            while end < n:
                l3 = max(l1, l2)
                if ok(start, l1, l2, l3):
                    start, l1, l2 = start + l1, l2, l3
                elif ok(start, l1, l2, l3 + 1):
                    start, l1, l2 = start + l1, l2, l3 + 1
                else:
                    return False
                end = start + l1 + l2
            return True


        for i in xrange(1, n):
            for j in xrange(1, n):
                if valid(i, j):
                    return True

        return False

print Solution().isAdditiveNumber("121224036")
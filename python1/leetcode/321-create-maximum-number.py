class Solution(object):
    def maxNumber(self, nums1, nums2, k):

        n1, n2 = len(nums1), len(nums2)
        a, b = map(str, nums1[::-1]), map(str, nums2[::-1])

        f1 = [''] * (k + 1)
        f2 = [''] * (k + 1)

        prev = [''] * (n1 + 1)
        for t in xrange(1, k + 1):
            curr = [''] * (n1 + 1)
            for i in xrange(t, n1 + 1):
                curr[i] = max(curr[i - 1], a[i - 1] + prev[i - 1])
            prev = curr
            f1[t] = curr[-1]

        prev = [''] * (n2 + 1)
        for t in xrange(1, k + 1):
            curr = [''] * (n2 + 1)
            for i in xrange(t, n2 + 1):
                curr[i] = max(curr[i - 1], b[i - 1] + prev[i - 1])
            prev = curr
            f2[t] = curr[-1]

        result = ''
        for t in xrange(k + 1):
            x1, x2 = f1[t], f2[k - t]
            if len(x1) + len(x2) == k:
                i, j = 0, 0
                r = ''
                while x1 and x2:
                    if x1 > x2:
                        r += x1[0]
                        x1 = x1[1:]
                    else:
                        r += x2[0]
                        x2 = x2[1:]
                r += x1 + x2
                if r > result:
                    result = r

        return map(int, list(result))



print Solution().maxNumber([6,7],
[6,0,4],
5)

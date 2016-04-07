class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):

        n = len(s)
        f = [[False for i in range(n)] for j in range(n)]

        for i in range(n):
            f[i][i] = True
            for j in range(1, i+1):
                if i+j >= n:
                    break
                if s[i+j] == s[i-j]:
                    f[i-j][j+i] = True
                else:
                    break
            for j in range(1, i+1):
                if i+j-1 >= n:
                    break
                if s[i+j-1] == s[i-j]:
                    f[i-j][j+i-1] = True
                else:
                    break
        r = [-1] + [n-1] * n
        for i in range(n):
            for j in range(0, i+1):
                if f[i-j][i]:
                    if r[i+1] > r[i-j] + 1:
                        r[i+1] = r[i-j]+1

        return r[n]


t = Solution()
t.minCut('aaba')
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):

        increasing = []
        i = 0
        n = len(height)
        r = 0
        while (i<=n):
            if not increasing or (i < n and height[increasing[-1]] < height[i]):
                increasing.append(i)
                i += 1
            else:
                last = increasing.pop()
                if increasing:
                    r = max(r, height[last]*(i - increasing[-1]- 1))
                else:
                    r = max(r, height[last] * i)

        return r


h = [1, 2, 1.5, 4, 3]
print Solution().largestRectangleArea(h)
class Solution:
    # @return an integer
    def maxArea(self, height):
        r, left, right = 0, 0, len(height) - 1
        while left < right:
            r = max(r, min(height[left], height[right]) * (right-left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return r


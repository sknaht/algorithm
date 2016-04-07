class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums: return 0
        c=[nums[0]]
        for i in nums:
            if i<=c[0]:
                c[0]=i
            elif i>c[-1]:
                c+=i,
            else:
                index=self.bs(c ,0, len(c), i)
                c[index]=min(i, c[index])
        return len(c)

    def bs(self, nums, l, r, key):
        while r-l>1:
            m=(r+l)/2
            if nums[m]>=key:
                r=m
            else:
                l=m
        return r

print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        if len(nums) < 2:
            return
        for i in xrange(len(nums) - 1, 0, -1):
            if nums[i-1] < nums[i]:
                d = i
                for j in xrange(i + 1, len(nums)):
                    if nums[i-1] < nums[j] <= nums[d]:
                        d = j
                nums[i - 1], nums[d] = nums[d], nums[i-1]
                for j in xrange(len(nums) - i - 1, 0, -1):
                    for k in xrange(j):
                        if nums[i + k + 1] < nums[i + k]:
                            nums[i + k + 1], nums[i + k] = nums[i + k], nums[i + k + 1]
                return
        h, t = 0, len(nums) - 1
        while h < t:
            nums[h], nums[t] = nums[t], nums[h]
            h, t = h + 1, t - 1

Solution().nextPermutation([3, 2, 0, 1])
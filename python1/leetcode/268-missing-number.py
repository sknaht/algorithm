class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while i < len(nums):
            while nums[i] < i:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            i += 1
        for i in xrange(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

print Solution().missingNumber([1,0])
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        def traceback(result, path, nums, index):
            result.append([x for x in path])
            for i in xrange(index, len(nums)):
                traceback(result, path + [nums[i]], nums, i + 1)

        nums.sort(reverse=True)
        traceback(result, [], nums, 0)
        return result

print Solution().subsets([1,2,3])
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        a = [nums[0]]
        indexs = [0]

        for i in xrange(k):
            if nums[i] > a[0]:
                a[0] = nums[i]
                indexs[0] = i

        result = [a[0]]

        for i in xrange(k, len(nums)):

            if indexs[0] < i:
                a.pop(0)
                indexs.pop(0)

            while a and a[-1] < nums[i]:
                a.pop()
                indexs.pop()

            a.append(nums[i])
            indexs.append(i)

            result.append(a[0])

        return result







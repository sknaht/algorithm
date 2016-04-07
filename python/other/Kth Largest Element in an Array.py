class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        if not nums:
            return

        def find(nums, k):
            pivot, left, right = nums[0], 0, len(nums) - 1
            while left < right:
                while left < right and nums[right] >= pivot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= pivot:
                    left += 1
                nums[right] = nums[left]
            nums[left] = pivot
            if len(nums) - left == k:
                return nums[left]
            if len(nums) - left > k:
                return find(nums[left + 1:], k)
            else:
                return find(nums[:left], k - (len(nums) - left))

        return find(nums, k)

print Solution().findKthLargest([3,2,1,5,6,4], 1)


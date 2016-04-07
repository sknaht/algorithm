class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        m1, m2 = None, None
        n1, n2 = 0, 0
        for num in nums:
            if m1 is None:
                m1, n1 = num, 1
            elif m1 == num:
                n1 += 1
            elif m2 is None:
                m2, n2 = num, 1
            elif m2 == num:
                n2 += 1
            elif n1 < n2:
                n1 -= 1
                if n1 == 0:
                    m1, n1 = num, 1
            else:
                n2 -= 1
                if n2 == 0:
                    m2, n2 = num, 1

        r = []
        if n1 > len(nums) / 3:
            r.append(m1)
        if n2 > len(nums) / 3:
            r.append(m2)
        return r


print Solution().majorityElement([4,1, 2,1])
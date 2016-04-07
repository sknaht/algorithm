"""
radix sort
"""
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
            
        def sort(a, radix=10):
            import math
            K = int(math.ceil(math.log(max(a), radix)))
            buckets = [[] for i in xrange(radix)]
            t = 1
            for i in xrange(K + 1):
                for v in a:
                    buckets[(v / t) % radix].append(v)
                del a[:]
                for b in buckets:
                    a.extend(b)
                buckets = [[] for j in xrange(radix)]
                t *= radix
                
        sort(nums)
        ans = 0
        for i in xrange(1, len(nums)):
            ans = max(ans, nums[i] - nums[i - 1])
            
        return ans

Solution().maximumGap([1,100])
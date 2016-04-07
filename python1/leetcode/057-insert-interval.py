# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]

        i = 0
        while i < len(intervals):
            if newInterval.start < intervals[i].start:
                intervals.insert(i, newInterval)
                break
            i += 1
        else:
            intervals.append(newInterval)

        ans = []
        for i in xrange(len(intervals)):
            if not ans or ans[-1].end < intervals[i].start:
                ans.append(intervals[i])
            else:
                ans[-1].end = max(ans[-1].end, intervals[i].end)

        return ans


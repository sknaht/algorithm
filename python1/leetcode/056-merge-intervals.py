# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        def quicksort(start, end):
            if start >= end:
                return
            s, e = start, end
            t = intervals[e]
            while s < e:
                while s < e and intervals[s].start <= t.start:
                    s += 1
                if s >= e:
                    break
                intervals[e] = intervals[s]
                e -= 1
                while s < e and intervals[e].start >= t.start:
                    e -= 1
                if s >= e:
                    break
                intervals[s] = intervals[e]
                s += 1
            intervals[e] = t
            quicksort(start, e - 1)
            quicksort(e + 1, end)

        quicksort(0, len(intervals) - 1)
        ans = []
        for t in intervals:
            if not ans or t.start > ans[-1].end:
                x = Interval(t.start, t.end)
                ans.append(x)
            else:
                ans[-1].end = max(ans[-1].end, t.end)
        return ans


Solution().merge([Interval(1,4), Interval(2,4)])

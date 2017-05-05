"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

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
        
        if not intervals:
            return []
            
        intervals.sort(key = lambda x:x.start)
        ret = [intervals[0]]
        for cur in intervals[1:]:
            pre = ret[-1]
            if cur.start <=pre.end:
                pre.end = max(pre.end,cur.end)
            else:
                ret.append(cur)
        
        return ret

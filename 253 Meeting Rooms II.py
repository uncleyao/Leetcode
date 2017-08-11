"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        left = [i.start for i in intervals]
        right = [j.end for j in intervals]
        left.sort()
        right.sort()
        result = 0
        j = 0
        for i in range(len(left)):
            if left[i] < right[j]:
                result+=1
            else:
                j+=1
        return result

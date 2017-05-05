"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""

__author__ = 'yyao'



class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "[%d, %d]" % (self.start, self.end)

    def __repr__(self):
        return repr(self.__str__())

class Solution(object):
    def insert(self, itvls, newItvl):
        s,e = newItvl.start, newItvl.end
        left = [x for x in itvls if x.end <s]
        right = [y for y in itvls if y.start > e]
        if len(left) + len(right)!= len(itvls):
            s = min(s, itvls[len(left)].start)
            e = max(e,itvls[-len(right)-1].end)
        return left + [s,e] + right

if __name__ == "__main__":
    lst = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    insert = [4, 9]
    lst_interval = []
    for item in lst:
        lst_interval.append(Interval(item[0], item[1]))
    print(lst_interval)
    print(Solution().insert(lst_interval, Interval(insert[0], insert[1])))

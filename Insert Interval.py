#!/usr/bin/python

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        res = []
        n = len(intervals)
        for i in range(n):
            if intervals[i].end < newInterval.start:
                res.append(intervals[i])
            elif intervals[i].start > newInterval.end:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            else:
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
        res.append(newInterval)
        return res

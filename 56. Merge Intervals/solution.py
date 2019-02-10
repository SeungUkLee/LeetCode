# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if not intervals:
            return []
        
        sorted_intervals: List[Interval] = sorted(intervals, 
                                                  key=lambda x: x.start)
        res: List[Interval] = [sorted_intervals[0]]
        
        for i in range(1, len(sorted_intervals)):
            if self.is_can_overlapping(res[-1], sorted_intervals[i]):
                res[-1] = Interval(res[-1].start, max(sorted_intervals[i].end, res[-1].end))
            else:
                res.append(sorted_intervals[i])
        return res
                                           
    def is_can_overlapping(self, l1, l2) -> bool:
        if l1.start <= l2.start <= l1.end:
            return True
        return False

